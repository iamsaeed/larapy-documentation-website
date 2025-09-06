// Custom JavaScript for Larapy Documentation Website

document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Larapy Documentation Website loaded successfully!');
    
    // Initialize tooltips
    const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltips.forEach(tooltip => {
        new bootstrap.Tooltip(tooltip);
    });
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add loading state to buttons
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('click', function() {
            if (this.getAttribute('href') && this.getAttribute('href').startsWith('http')) {
                this.innerHTML = '<span class="loading"></span> Loading...';
                setTimeout(() => {
                    this.innerHTML = this.dataset.originalText || this.innerHTML.replace('<span class="loading"></span> Loading...', '');
                }, 2000);
            }
        });
    });
    
    // Code copy functionality (for future use)
    function addCopyButtons() {
        const codeBlocks = document.querySelectorAll('pre code');
        codeBlocks.forEach(codeBlock => {
            const button = document.createElement('button');
            button.className = 'btn btn-sm btn-outline-secondary position-absolute top-0 end-0 m-2';
            button.innerHTML = '<i class="bi bi-clipboard"></i>';
            button.title = 'Copy to clipboard';
            
            button.addEventListener('click', () => {
                navigator.clipboard.writeText(codeBlock.textContent).then(() => {
                    button.innerHTML = '<i class="bi bi-check"></i>';
                    button.className = 'btn btn-sm btn-success position-absolute top-0 end-0 m-2';
                    setTimeout(() => {
                        button.innerHTML = '<i class="bi bi-clipboard"></i>';
                        button.className = 'btn btn-sm btn-outline-secondary position-absolute top-0 end-0 m-2';
                    }, 2000);
                });
            });
            
            const pre = codeBlock.parentElement;
            pre.style.position = 'relative';
            pre.appendChild(button);
        });
    }
    
    // Initialize copy buttons after a short delay to ensure Prism has loaded
    setTimeout(addCopyButtons, 500);
    
    // Add fade-in animation to cards
    const cards = document.querySelectorAll('.card');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
    
    // Console welcome message
    console.log(`
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║     Welcome to Larapy Documentation Website!        ║
    ║                                                      ║
    ║     Laravel's elegant syntax meets Python's         ║
    ║     simplicity in this powerful web framework.      ║
    ║                                                      ║
    ║     🐍 Built with Python                            ║
    ║     🚀 Powered by Larapy Framework                  ║
    ║     📚 Documentation Coming Soon                    ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
    `);
});