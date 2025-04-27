// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });
    
    // Highlight active nav link
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentLocation) {
            link.classList.add('active');
        }
    });
    
    // Add year to footer copyright
    const yearElement = document.querySelector('.copyright-year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }
    
    // Handle card clicks - navigate to article detail page
    const articleCards = document.querySelectorAll('.card');
    articleCards.forEach(card => {
        const cardLink = card.querySelector('a[href^="/article/"]');
        if (cardLink) {
            card.style.cursor = 'pointer';
            card.addEventListener('click', function(e) {
                // Don't navigate if user clicked on a tag link
                if (e.target.tagName === 'A' && e.target.classList.contains('badge')) {
                    return;
                }
                // Navigate to article detail page
                window.location.href = cardLink.getAttribute('href');
            });
        }
    });
}); 