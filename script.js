// Import Locomotive Scroll (assuming it's installed via npm or a CDN is used)
import LocomotiveScroll from 'locomotive-scroll';

// Initialize Locomotive Scroll
const scroll = new LocomotiveScroll({
  el: document.querySelector('[data-scroll-container]'),
  smooth: true,
  getDirection: true,
});

// Optional: Log scrolling direction
scroll.on('scroll', (event) => {
  console.log('Scrolling direction:', event.direction);
});

// Animate sections on scroll
const sections = document.querySelectorAll('[data-scroll-section]');

sections.forEach((section, index) => {
  section.style.opacity = 0;
  section.style.transform = 'translateY(50px)';
  scroll.on('call', (func) => {
    if (func === `section-${index}`) {
      section.style.opacity = 1;
      section.style.transform = 'translateY(0)';
      section.style.transition = 'all 0.6s ease';
    }
  });
});
