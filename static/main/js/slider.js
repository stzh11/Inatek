document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelector('.slides');
    const images = document.querySelectorAll('.slides img');
    const prevBtn = document.querySelector('.slide-btn.prev');
    const nextBtn = document.querySelector('.slide-btn.next');
    const heroSection = document.getElementById('hero');

    let index = 0;

    const backgrounds = [
        heroSection.dataset.bg1,
        heroSection.dataset.bg2,
        heroSection.dataset.bg3
    ];

    function updateSlide() {
        console.log('✅ Смена фона на:', backgrounds[index]);
        slides.style.transform = `translateX(-${index * 100}%)`;
        heroSection.style.backgroundImage = `url('${backgrounds[index]}')`;
    }

    function nextSlide() {
        index = (index + 1) % images.length;
        updateSlide();
    }

    function prevSlide() {
        index = (index - 1 + images.length) % images.length;
        updateSlide();
    }

    if (nextBtn && prevBtn) {
        nextBtn.addEventListener('click', nextSlide);
        prevBtn.addEventListener('click', prevSlide);
    } else {
        console.warn('❌ Кнопки слайдера не найдены!');
    }

    // ⏱️ Автопрокрутка каждые 5 секунд
    setInterval(nextSlide, 7000);

    // Первая отрисовка
    updateSlide();
});
