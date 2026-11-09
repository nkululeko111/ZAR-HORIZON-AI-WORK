import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'ZAR HORIZON AI @WORK',
  description: 'Purpose-built AI digital employees for business and security.',
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en-ZA">
      <body>{children}</body>
    </html>
  );
}
