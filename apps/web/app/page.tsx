const products = [
  {
    number: '01',
    name: 'AI Business Partner',
    category: 'BUSINESS, BUILT FORWARD',
    description:
      'A capable partner for the work of starting, running and growing a business — from research and planning to day-to-day operations.',
    detail: 'For founders and ambitious teams',
    className: 'business',
  },
  {
    number: '02',
    name: 'AI Hacker',
    category: 'SECURITY, PROVEN',
    description:
      'A future red-team platform designed to help authorised teams assess their systems, understand risk and verify remediation.',
    detail: 'For authorised security testing',
    className: 'security',
  },
];

export default function Home() {
  return (
    <main>
      <nav className="topbar" aria-label="Main navigation">
        <a className="brand" href="#" aria-label="ZAR HORIZON AI at WORK home">
          <span className="brand-mark" aria-hidden="true">
            ZH
          </span>
          <span>
            <strong>ZAR HORIZON</strong>
            <small>AI @WORK</small>
          </span>
        </a>
        <a className="nav-link" href="#products">
          Our products <span aria-hidden="true">↘</span>
        </a>
      </nav>

      <section className="hero">
        <div className="hero-copy">
          <p className="eyebrow">
            <span className="status-dot" /> SOUTH AFRICAN TECHNOLOGY, BUILT FOR WHAT&apos;S NEXT
          </p>
          <h1>
            Good work
            <br />
            moves <span>horizons.</span>
          </h1>
          <p className="hero-description">
            Meet a new generation of digital employees, purpose-built to help people build business
            and strengthen security.
          </p>
          <a className="primary-link" href="#products">
            Discover the platform <span aria-hidden="true">↓</span>
          </a>
        </div>
        <div className="hero-visual" aria-hidden="true">
          <div className="orbit orbit-one" />
          <div className="orbit orbit-two" />
          <div className="orbit orbit-three" />
          <div className="visual-core">
            <span>ZH</span>
          </div>
          <div className="visual-caption">
            <span>INTELLIGENCE</span>
            <span>WITH INTENTION</span>
          </div>
          <span className="visual-coordinate">33°55&apos;S&nbsp; 18°25&apos;E</span>
        </div>
        <div className="hero-index">
          <span>01</span> / 02
        </div>
      </section>

      <section className="products" id="products">
        <div className="section-heading">
          <div>
            <p className="eyebrow">ONE PLATFORM. TWO SPECIALISTS.</p>
            <h2>Built for meaningful work.</h2>
          </div>
          <p className="section-intro">
            Shared foundations. Independent expertise. Each digital employee is designed around the
            work it is trusted to do.
          </p>
        </div>
        <div className="product-grid">
          {products.map((product) => (
            <article className={`product-card ${product.className}`} key={product.number}>
              <div className="card-topline">
                <span>{product.category}</span>
                <span>{product.number}</span>
              </div>
              <div className="card-symbol" aria-hidden="true">
                {product.className === 'business' ? '↗' : '⌁'}
              </div>
              <h3>{product.name}</h3>
              <p>{product.description}</p>
              <div className="card-footer">
                <span>{product.detail}</span>
                <span className="arrow" aria-hidden="true">
                  ↗
                </span>
              </div>
            </article>
          ))}
        </div>
      </section>

      <footer>
        <a className="brand footer-brand" href="#">
          <span className="brand-mark" aria-hidden="true">
            ZH
          </span>
          <span>
            <strong>ZAR HORIZON</strong>
            <small>AI @WORK</small>
          </span>
        </a>
        <p>Built with purpose in South Africa.</p>
        <span className="footer-note">© {new Date().getFullYear()} ZAR HORIZON (Pty) Ltd</span>
      </footer>
    </main>
  );
}
