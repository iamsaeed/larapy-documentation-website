// Application JavaScript

document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Larapy Application Loaded');
    
    // Add any global JavaScript functionality here
    
    // Example: CSRF token setup for AJAX requests
    const csrfToken = document.querySelector('meta[name="csrf-token"]');
    if (csrfToken) {
        // Set up CSRF token for fetch requests
        window.csrfToken = csrfToken.getAttribute('content');
    }
    
    // Example: Global error handler
    window.addEventListener('error', function(event) {
        console.error('Global error:', event.error);
    });
});

// Utility functions
const App = {
    // Example utility function
    showAlert: function(message, type = 'info') {
        const alert = document.createElement('div');
        alert.className = `alert alert-${type} alert-dismissible fade show`;
        alert.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        // Find a container for alerts or create one
        let alertContainer = document.getElementById('alerts');
        if (!alertContainer) {
            alertContainer = document.createElement('div');
            alertContainer.id = 'alerts';
            alertContainer.className = 'container mt-3';
            document.body.insertBefore(alertContainer, document.body.firstChild);
        }
        
        alertContainer.appendChild(alert);
        
        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            if (alert.parentNode) {
                alert.remove();
            }
        }, 5000);
    }
};

// Make App available globally
window.App = App;