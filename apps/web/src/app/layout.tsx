import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import "./globals.css";

export const revalidate = 300;

export const metadata: Metadata = {
  title: {
    default: "Liquid Snippets by ALSEL｜日本初の Shopify Liquid 日本語リファレンス",
    template: "%s | Liquid Snippets by ALSEL",
  },
  description:
    "Shopify 公式ドキュメントを完全カバーする、検索可能な日本語リファレンス。フィルター・タグ・オブジェクトの仕様、コミュニティ実装例まで網羅。",
  metadataBase: new URL("https://liquid-jp.jp"),
  openGraph: {
    title: "Liquid Snippets by ALSEL｜日本初の Shopify Liquid 日本語リファレンス",
    description:
      "Shopify 公式ドキュメントを完全カバーする、検索可能な日本語リファレンス。",
    url: "https://liquid-jp.jp",
    siteName: "Liquid Snippets by ALSEL",
    type: "website",
    locale: "ja_JP",
  },
  twitter: {
    card: "summary_large_image",
    title: "Liquid Snippets by ALSEL｜日本初の Shopify Liquid 日本語リファレンス",
    description:
      "Shopify 公式ドキュメントを完全カバーする、検索可能な日本語リファレンス。",
  },
  icons: {
    icon: "/icon.svg",
    apple: "/icon.svg",
  },
};

export default async function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="ja" className="h-full antialiased">
      <body className="min-h-full flex flex-col bg-white text-slate-900">
        <header className="border-b border-slate-200 bg-white sticky top-0 z-10">
          <div className="max-w-6xl mx-auto px-6 py-3 flex items-center justify-between gap-4">
            <Link
              href="/"
              className="flex items-center hover:opacity-80 shrink-0"
              aria-label="Liquid Snippets by ALSEL — ホームへ"
            >
              <Image
                src="/logo.svg"
                alt="Liquid Snippets by ALSEL"
                width={280}
                height={64}
                priority
                className="h-12 md:h-14 w-auto"
              />
            </Link>
            <nav className="flex items-center gap-6 text-sm text-slate-600">
              <Link href="/category" className="hover:text-violet-700">
                カテゴリ
              </Link>
              <Link href="/about" className="hover:text-violet-700">
                About
              </Link>
            </nav>
          </div>
        </header>
        <div className="flex-1">{children}</div>
        <footer className="border-t border-slate-200 mt-12">
          <div className="max-w-6xl mx-auto px-6 py-8 flex flex-col md:flex-row justify-between gap-4 text-sm text-slate-600">
            <div>
              <div className="font-bold text-slate-900">Liquid Snippets by ALSEL</div>
              <div className="mt-1 text-slate-500">
                日本初の Shopify Liquid 日本語リファレンス。
              </div>
              <div className="mt-2 text-xs text-slate-500 max-w-md leading-relaxed">
                ※ 本サイトは Shopify Inc. の公式サイトではありません。
                Liquid は Shopify Inc. の商標です。掲載コードは各 OSS の MIT ライセンスに基づきます。
              </div>
              <div className="mt-2 text-xs">© 2026 ALSEL Inc. / 株式会社ALSEL</div>
            </div>
            <div className="flex flex-wrap gap-x-6 gap-y-2">
              <Link href="/about" className="hover:text-violet-700">About</Link>
              <Link href="/terms" className="hover:text-violet-700">利用規約</Link>
              <Link href="/privacy" className="hover:text-violet-700">プライバシー</Link>
              <a
                href="https://agent-skills.jp"
                target="_blank"
                rel="noopener noreferrer"
                className="hover:text-violet-700"
              >
                Agent Skills by ALSEL ↗
              </a>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
