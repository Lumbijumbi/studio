export type QueueOptions = {
  concurrency?: number;
};

type TaskRunner = () => Promise<void>;

export class Queue {
  private concurrency: number;
  private running = 0;
  private waiting: TaskRunner[] = [];

  constructor(options: QueueOptions = {}) {
    this.concurrency = Math.max(1, options.concurrency ?? 1);
  }

  add<T>(task: () => Promise<T>): Promise<T> {
    return new Promise<T>((resolve, reject) => {
      const runner: TaskRunner = async () => {
        this.running++;
        try {
          const result = await task();
          resolve(result);
        } catch (err) {
          reject(err instanceof Error ? err : new Error(String(err)));
        } finally {
          this.running--;
          this.drain();
        }
      };

      this.waiting.push(runner);
      this.drain();
    });
  }

  private drain() {
    while (this.running < this.concurrency && this.waiting.length > 0) {
      // Safe to use ! because we check waiting.length > 0 in the while condition
      const next = this.waiting.shift()!;
      void next();
    }
  }

  get size(): number {
    return this.waiting.length + this.running;
  }
}
