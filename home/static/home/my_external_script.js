const toggleButton = document.getElementsByClassName('menu-toggle')[0]
const navbarLinks = document.getElementsByClassName('navbar-links')[0]

toggleButton.addEventListener("click", () => {
  navbarLinks.classList.toggle('active')
})


const facebook = document.querySelector('.facebook');
const linkedin = document.querySelector('.linkedin');
const twitter = document.querySelector('.twitter');
const whatsapp = document.querySelector('.whatsapp');

function share() {
  let articleImg = encodeURI(document.querySelector('.main-image'));
  const postUrl = encodeURI(document.location.href);
  let postTitle =  encodeURI('Hey, check this out!');
  let hashtags = encodeURI('IvoTechClub')
  
  facebook.setAttribute("href",
   `https://www.facebook.com/sharer.php?u=${postUrl}`);
  twitter.setAttribute("href",
    `https://twitter.com/share?url=${postUrl}&text=${postTitle}&hashtags=${hashtags}`);
  linkedin.setAttribute("href",
    `https://www.linkedin.com/shareArticle?url=${postUrl}&title=${postTitle}`);
  whatsapp.setAttribute("href",
    `https://api.whatsapp.com/send?text=${postTitle} ${postUrl}`)
}

share()