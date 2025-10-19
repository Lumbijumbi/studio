import { Queue as QueueImpl } from 'queue-typescript';

export interface QueueOptions {
  concurrency?: number;
}

export class Queue<T = void> {
  private queue: QueueImpl<() => Promise<T>>;
  private concurrency: number;
  private running: number = 0;

  constructor(options: QueueOptions = {}) {
    this.concurrency = options.concurrency || 1;
    this.queue = new QueueImpl<() => Promise<T>>();
  }

  async add(fn: () => Promise<T>): Promise<T> {
    return new Promise<T>((resolve, reject) => {
      const task = async () => {
        try {
          const result = await fn();
          resolve(result);
        } catch (error) {
          reject(error);
        } finally {
          this.running--;
          this.processNext();
        }
      };

      this.queue.enqueue(task as () => Promise<T>);
      this.processNext();
    });
  }

  private processNext(): void {
    if (this.running >= this.concurrency) {
      return;
    }

    if (this.queue.length === 0) {
      return;
    }

    const task = this.queue.dequeue();
    if (task) {
      this.running++;
      task();
    }
  }
}
