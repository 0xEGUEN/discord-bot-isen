// Check bot status on page load
document.addEventListener('DOMContentLoaded', function() {
    checkBotStatus();
    setupCommandFilters();
});

// Check bot status
async function checkBotStatus() {
    try {
        const response = await fetch('/api/status');
        const data = await response.json();
        
        const statusElement = document.getElementById('bot-status');
        if (data.status === 'online') {
            statusElement.textContent = 'Bot Status: Online ✓';
            statusElement.style.color = '#10b981';
        } else {
            statusElement.textContent = 'Bot Status: Offline ✗';
            statusElement.style.color = '#ef4444';
        }
    } catch (error) {
        console.error('Error checking bot status:', error);
        document.getElementById('bot-status').textContent = 'Bot Status: Unable to check';
    }
}

// Setup command filter buttons
function setupCommandFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const commandCards = document.querySelectorAll('.command-card');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');
            
            // Get filter value
            const filter = this.getAttribute('data-filter');
            
            // Filter commands
            commandCards.forEach(card => {
                if (filter === 'all' || card.getAttribute('data-type') === filter) {
                    card.classList.remove('hidden');
                    // Add animation
                    card.style.animation = 'none';
                    setTimeout(() => {
                        card.style.animation = 'fadeIn 0.3s ease-in';
                    }, 10);
                } else {
                    card.classList.add('hidden');
                }
            });
        });
    });
}

// Add fadeIn animation
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);

// Refresh status every 30 seconds
setInterval(checkBotStatus, 30000);
