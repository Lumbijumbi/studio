/**
 * A simple async queue with concurrency control
 */
export class Queue<T> {
  private concurrency: number;
  private running: number = 0;
  private queue: Array<() => Promise<T>> = [];
  private results: T[] = [];

  constructor(options: { concurrency: number }) {
    this.concurrency = options.concurrency;
  }

  async add(fn: () => Promise<T>): Promise<T> {
    return new Promise<T>((resolve, reject) => {
      const task = async () => {
        try {
          const result = await fn();
          resolve(result);
          return result;
        } catch (error) {
          reject(error);
          throw error;
        } finally {
          this.running--;
          this.processNext();
        }
      };

      this.queue.push(task);
      this.processNext();
    });
  }

  private async processNext() {
    if (this.running >= this.concurrency || this.queue.length === 0) {
      return;
    }

    this.running++;
    const task = this.queue.shift();
    if (task) {
      task();
    }
  }
}
