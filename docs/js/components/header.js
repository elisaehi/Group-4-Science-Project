function createHeader() {
    const header = document.createElement('header');
    header.classList.add('site-header');

    const logo = document.createElement('h1');
    logo.textContent = 'Food Processing & Preservation';
    header.appendChild(logo);

    const nav = document.createElement('nav');
    const links = [
        { href: 'overview.html', text: 'Overview' },
        { href: 'processing.html', text: 'Processing' },
        { href: 'preservation.html', text: 'Preservation' },
        { href: 'food-safety.html', text: 'Food Safety' },
        { href: 'resources.html', text: 'Resources' }
    ];

    links.forEach(link => {
        const a = document.createElement('a');
        a.href = link.href;
        a.textContent = link.text;
        nav.appendChild(a);
    });

    header.appendChild(nav);
    return header;
}

export default createHeader;