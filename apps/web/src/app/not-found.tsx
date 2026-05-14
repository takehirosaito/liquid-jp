import Link from "next/link";

export default function NotFound() {
  return (
    <main className="max-w-3xl mx-auto px-6 py-20 text-center">
      <h1 className="text-5xl font-bold text-violet-700 mb-4">404</h1>
      <p className="text-lg text-slate-700 mb-8">
        お探しのページは見つかりませんでした。
      </p>
      <div className="flex gap-4 justify-center flex-wrap">
        <Link
          href="/"
          className="px-6 py-3 bg-violet-700 text-white rounded-lg hover:bg-violet-800"
        >
          ホームに戻る
        </Link>
        <Link
          href="/category"
          className="px-6 py-3 border border-slate-300 rounded-lg hover:bg-slate-100"
        >
          カテゴリから探す
        </Link>
      </div>
    </main>
  );
}
