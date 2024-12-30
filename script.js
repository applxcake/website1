// Smooth Scroll
document.querySelectorAll('.nav-links a').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    target.scrollIntoView({ behavior: 'smooth' });
  });
});

import LocomotiveScroll from 'locomotive-scroll';
import gsap from 'gsap';

const scroll = new LocomotiveScroll({
  el: document.querySelector('[data-scroll-container]'),
  smooth: true,
  lerp: 0.1, // Adjust for smoother scrolling
});

// GSAP Animations
scroll.on('call', (func) => {
  if (func === 'animateHero') {
    gsap.fromTo(
      '.hero-content',
      { opacity: 0, y: 50 },
      { opacity: 1, y: 0, duration: 1, ease: 'power3.out' }
    );
  }
});

// Trigger GSAP animations for sections on enter
scroll.on('scroll', ({ currentElements }) => {
  for (const key in currentElements) {
    if (currentElements[key].el.classList.contains('features-container')) {
      gsap.fromTo(
        '.feature-item',
        { opacity: 0, y: 50 },
        { opacity: 1, y: 0, duration: 1, stagger: 0.2 }
      );
    }
  }
});
