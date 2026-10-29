document.querySelectorAll('[data-gallery]').forEach((gallery) => {
  const image = gallery.querySelector('figure img');
  const imageLink = gallery.querySelector('.image-link');
  const caption = gallery.querySelector('figcaption');
  gallery.querySelectorAll('button[data-image]').forEach((button) => {
    button.addEventListener('click', () => {
      gallery.querySelectorAll('button[data-image]').forEach((item) => {
        item.classList.remove('selected');
        item.setAttribute('aria-pressed', 'false');
      });
      button.classList.add('selected');
      button.setAttribute('aria-pressed', 'true');
      image.src = button.dataset.image;
      image.alt = button.dataset.alt;
      imageLink.href = button.dataset.image;
      caption.textContent = button.dataset.description;
    });
  });
});
