
<!DOCTYPE html>
<!--HTML-->
<html lang="en">
  <head>
      <meta charset="utf-8">
      <meta content="width=device-width, initial-scale=1.0" name="viewport">
      <meta content="" name="description">
      <meta content="" name="keywords">
      <!--CSS FILE-->
      <link href="https://res.cloudinary.com/storagemanagementcontainer/raw/upload/v1627722425/styles_n5guzo.css"  rel="stylesheet"  >
      <link href='https://fonts.googleapis.com/css?family=Roboto+Slab&display=swap' >
      <link rel="stylesheet" href="https://res.cloudinary.com/storagemanagementcontainer/raw/upload/v1627723191/formstyles_akkwuz.css" />
      <script src='https://res.cloudinary.com/storagemanagementcontainer/raw/upload/v1627616012/form_clkn7f.js'></script>
 <style>a:link{
  font-weight:bold;
}
 @media all and (max-width: 599px) and (min-width: 0px) {
     form{
  
         margin: 1%;
     }
 }
 .messagesweb{
    color: #909FBB;
    font-size: 18px;
    background-color: #EBC3C2;
    width: 100%;
}
 }
  .profile {
	  background-color: #fafafa;
	  border-radius: 1rem;
 }
 .profile__header {
     height:2rem
 }
  .profile__image {
	  padding: 2rem;
	  padding-bottom: 0;
	  width: 30rem;
	  height: 30rem;
 }
  .profile__image img {
	 /* position: absolute;*/
	  border-radius: 1rem;
	  width: inherit;
	  height: 30rem;
	  /*transform: translateY(-4.5rem);*/
	  object-fit: cover;
      margin: auto;
	  box-shadow: -7px 6px 12px -1px rgba(40, 40, 40, 0.55);
	  /*transition: all 0.5s ease;*/
 }
  .profile__image img:hover {
	  transform: translateY(-4.5rem) scale(1.05);
 }
  .profile p {
	  padding: 1rem;
	  padding-bottom: 0;
	  font-size: 1.5rem;
	  text-align: center;
 }
  .profile__name p {
	  color: #EBC3C2;
	  font-weight: bold;
	  font-size: 2.2rem;
	  text-align: center;
 }


</style>
</head>
    <!--BODY-->
  <body class="container">
    <!-- HEADER NAV -->
    <header class="header">
        <nav class="header__nav">
            <ul class="nav__sidenav nav--right">
                <li><a href="/" class="header__logo"> <img   class='header__img' src="https://res.cloudinary.com/storagemanagementcontainer/image/upload/v1627668649/verticalheadcrest_zegh6d.svg" alt="" /></a></li>
                <div class="header__links">
                <li class="header__link"><a href="about" >About</a></li>
                <li class="header__link"><a href="clients" >Clients</a></li>
                <li class="header__link"><a href="calendar" >Book</a></li>
                <li class="header__link"><a href="contact" >Contact Us</a></li>

                <li class="header__link"><a href="register" >Create Account</a></li>
                <li><a href="login" class="header__link">Login</a></li>

                <li class="header__link hide-3"><a href="#" id="nav-bag" ><img src="https://res.cloudinary.com/dmoo9az8w/image/upload/v1475715814/shopping_bag_cuw7pb.svg" alt="shopping" /></a></li>
                </div>

                <p class="header__welcome hide-3">Bonjour! Welcome to Madeleine Salon de Coiffure</p>

            </ul>
        </nav>
    </header>
    <body>
        <br>
        <br>
<!--MAIN-->
    <main class="mainsection"><br>
            <div class="profile">
                <h2 class='profile__header'>Profile Information:</h2><br><br>
                <div class="profile__image"><img src="https://res.cloudinary.com/storagemanagementcontainer/image/upload/v1627794758/profilepic_lhfmad.jpg"/></div>
                <div class="profile__name"><p></p></div>
                <p></p>
                <p>vous n'avez pas de rendez-vous programmé</p>
                <p>You have no appointments scheduled with Salon de Madeleine</p>
                <p>si vous souhaitez en programmer un, rendez-vous sur la page de réservation</p>
                <br>
                <a href="book"<button type="submit" class="submit-btn">Schedule Appointment</button></a>
            </div>


    </main>
<!--FOOTER-->
        <footer id="footer">
                <div id="footer-utility">
                    <div class="footer__chat">
                        <ul class="footer__ul"><h3 class="footer__left">À propos de nous</h3>
                            <li class="footer__li"><a class="footer__a" href="#">Politique de confidentialité</a></li>
                            <li class="footer__li"><a class="footer__a" href="#">Termes et conditions</a></li>
                            <li class="footer__li"> <img class="footer__chat-img-icon footer__li" width="18" height="14" src="https://res.cloudinary.com/cloudinary-account/image/upload/v1469462241/msg_jn0whe.svg" href="#" />Chat</li>
                            <li class="footer__li"> <img class="footer__chat-img-icon footer__li" width="15" height="15" src="https://res.cloudinary.com/cloudinary-account/image/upload/v1469462243/phone_zfj4ey.svg" href="#" />1-253-306-3470</li>
                        </ul>
                    </div>
                    <div class="footer__partition"></div>
                    <div class="footer__about">
                        <ul class="footer__ul">
                            <h3 class="footer__left">Madeleine Dupont</h3>
                            <li class="footer__li"><a class="footer__a" href="#">madeleinesalondecoiffure@gmail.com</a></li>
                            <li class="footer__li"><a class="footer__a" href="#">© 2021, Madeleine Salon de Coiffure</a></li>
                        </ul>
                    </div>
                    <div class="footer__partition"></div>
                    <div class="footer__card">
                        <ul class="footer__ul">
                            <h3 class="footer__left">À propos de nous</h3>
                            <li class="footer__li"><a class="footer__a" href="#">Politique de confidentialité</a></li>
                            <li class="footer__li"><a class="footer__a" href="#">Termes et conditions</a></li>
                        </ul>
                    </div>
                </div>
                <a class="footer__a" class="" href="/"><img class='footer__logo' src="https://res.cloudinary.com/storagemanagementcontainer/image/upload/v1627668880/skeletoncrest_t9zecb.svg" alt="" /></a>
                <div id="footer-newsletter-social">
                    <div id="footer-newsletter">
                        <h3 class="footer__center">Get more deals with Madeleine</h3>
                        <div class='footer__enter'>
                            <input type="text" placeholder="Enter email address" class="getemailform"/>
                            <input class="enteremailbutton" type="submit" value="Sign Up" />
                        </div>
                    </div>
                    <div id="footer-social">
                        <a class="footer__a" href="https://www.facebook.com/madeleine.beach.3" target="_blank" > <img width="34" height="34" src="https://res.cloudinary.com/storagemanagementcontainer/image/upload/v1627669349/facebook_eknuzn_drzww6.svg" alt="facebook" /></a>
                        <a class="footer__a" href="https://twitter.com/madecoiffure" target="_blank"> <img width="34" height="34" src="https://res.cloudinary.com/storagemanagementcontainer/image/upload/v1627669267/twitter_nfohqw_wdseyj.svg" alt="twitter" /></a> 
                        <a class="footer__a" href="https://pin.it/5qgAohs" target="_blank"> <img width="34" height="34" src="https://res.cloudinary.com/dmoo9az8w/image/upload/v1475715814/pinterest_vtom0c.svg" alt="pintrest" /></a > 
                        <a class="footer__a" href="https://www.instagram.com/madeleinebeachh/" target="_blank" > <img width="34" height="34" src="https://res.cloudinary.com/storagemanagementcontainer/image/upload/v1627669343/instagram_u4wt1i_br0ox6.svg" alt="instagram"/> </a>
                        <a class="footer__a" href="http://youtube.com/madeleinesalondecoiffure" target="_blank" > <img width="34" height="34" src="https://res.cloudinary.com/storagemanagementcontainer/image/upload/v1627677813/youtubeicon_u5ks3w.svg" alt="youtube" /></a>
                    </div>
                </div>       
                <div class="footer__border"></div>
                <div id="footer-copyright">
                    <div class="footer__law">
                    <ul class="footer__ul">
                        <li class="footer__li footer__copy"> © 2021 Madeleine Salon de Coiffure.</li>
                        <li class="footer__li footer__copy"> Privacy Policy | Terms + Conditions | Sitemap</li>
                        <li class=" footer__li footer__copy"> Washington | Transparency in Supply Chains Act</li>
                    </ul>
                    </div>
                </div>
                <br><br>
        </footer>
    </body>
</html>