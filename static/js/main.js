// Property Image Gallery
document.addEventListener('DOMContentLoaded', function() {
    const mainImage = document.querySelector('.property-details .main-image');
    const thumbnails = document.querySelectorAll('.property-details .thumbnail');
    
    if (mainImage && thumbnails.length > 0) {
        thumbnails.forEach(thumbnail => {
            thumbnail.addEventListener('click', function() {
                mainImage.src = this.src;
                thumbnails.forEach(t => t.classList.remove('active'));
                this.classList.add('active');
            });
        });
    }
});

// Property Search Form
document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.querySelector('.search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const searchParams = new URLSearchParams();
            
            for (let [key, value] of formData.entries()) {
                if (value) {
                    searchParams.append(key, value);
                }
            }
            
            window.location.href = `/properties/?${searchParams.toString()}`;
        });
    }
});

// Price Range Slider
document.addEventListener('DOMContentLoaded', function() {
    const priceRange = document.getElementById('priceRange');
    const priceValue = document.getElementById('priceValue');
    
    if (priceRange && priceValue) {
        priceRange.addEventListener('input', function() {
            priceValue.textContent = `€${this.value}`;
        });
    }
});

// Property Features Filter
document.addEventListener('DOMContentLoaded', function() {
    const featureCheckboxes = document.querySelectorAll('.feature-checkbox');
    const propertyCards = document.querySelectorAll('.property-card');
    
    if (featureCheckboxes.length > 0 && propertyCards.length > 0) {
        featureCheckboxes.forEach(checkbox => {
            checkbox.addEventListener('change', function() {
                const selectedFeatures = Array.from(featureCheckboxes)
                    .filter(cb => cb.checked)
                    .map(cb => cb.value);
                
                propertyCards.forEach(card => {
                    const cardFeatures = card.dataset.features.split(',');
                    const hasAllFeatures = selectedFeatures.every(feature => 
                        cardFeatures.includes(feature)
                    );
                    
                    card.style.display = hasAllFeatures ? 'block' : 'none';
                });
            });
        });
    }
});

// Contact Form Validation
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.querySelector('.contact-form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const name = this.querySelector('#name').value;
            const email = this.querySelector('#email').value;
            const message = this.querySelector('#message').value;
            
            if (!name || !email || !message) {
                alert('Please fill in all fields');
                return;
            }
            
            if (!isValidEmail(email)) {
                alert('Please enter a valid email address');
                return;
            }
            
            // Submit form
            this.submit();
        });
    }
});

// Email validation helper
function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', function() {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', function() {
            navbarCollapse.classList.toggle('show');
        });
        
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!navbarCollapse.contains(e.target) && !navbarToggler.contains(e.target)) {
                navbarCollapse.classList.remove('show');
            }
        });
    }
});

// Smooth Scrolling
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
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
}); 