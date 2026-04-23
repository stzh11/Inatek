document.addEventListener("DOMContentLoaded", () => {
    const slidesContainer = document.querySelector('.about-page-slider .slides');
    const slides = document.querySelectorAll('.about-page-slider .slide');
    let index = 0;
  
    function showSlide(i) {
      const offset = -i * 100;
      slidesContainer.style.transform = `translateX(${offset}%)`;
    }
  
    setInterval(() => {
      index = (index + 1) % slides.length;
      showSlide(index);
    }, 5000); // каждые 5 сек
  });
  
  