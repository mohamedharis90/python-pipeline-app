from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>CarePlus AI Hospital</title>

<link rel="preconnect" href="https://fonts.googleapis.com">

<link rel="preconnect"
href="https://fonts.gstatic.com"
crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap"
rel="stylesheet">

<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css">

<style>

*{

margin:0;
padding:0;
box-sizing:border-box;
font-family:'Poppins',sans-serif;

}

html{

scroll-behavior:smooth;

}

body{

background:#eef8ff;

overflow-x:hidden;

color:#222;

}

/* ---------------------------- */

:root{

--primary:#0077ff;
--secondary:#00bcd4;
--success:#00c853;
--danger:#ff1744;

--white:#ffffff;

--dark:#111827;

--glass:
rgba(255,255,255,.18);

}

/* ---------------------------- */

body::before{

content:"";

position:fixed;

top:-200px;
right:-200px;

width:650px;
height:650px;

border-radius:50%;

background:

radial-gradient(circle,
rgba(0,119,255,.18),
transparent);

z-index:-2;

animation:moveOne 14s infinite alternate;

}

body::after{

content:"";

position:fixed;

bottom:-250px;
left:-250px;

width:700px;
height:700px;

border-radius:50%;

background:

radial-gradient(circle,
rgba(0,255,180,.18),
transparent);

z-index:-2;

animation:moveTwo 15s infinite alternate;

}

@keyframes moveOne{

100%{

transform:

translate(-100px,90px);

}

}

@keyframes moveTwo{

100%{

transform:

translate(120px,-120px);

}

}

/* ---------------------------- */

.loader{

position:fixed;

top:0;
left:0;

width:100%;
height:100vh;

background:white;

display:flex;

justify-content:center;
align-items:center;

z-index:99999;

}

.loader span{

width:90px;
height:90px;

border-radius:50%;

border:10px solid #d7ecff;

border-top:

10px solid var(--primary);

animation:spin .8s linear infinite;

}

@keyframes spin{

100%{

transform:rotate(360deg);

}

}

/* ---------------------------- */

header{

position:fixed;

top:0;
left:0;

width:100%;

display:flex;

justify-content:space-between;

align-items:center;

padding:18px 60px;

background:

rgba(255,255,255,.82);

backdrop-filter:blur(20px);

box-shadow:

0 8px 25px rgba(0,0,0,.08);

z-index:1000;

}

.logo{

font-size:34px;

font-weight:800;

background:

linear-gradient(45deg,
#0077ff,
#00d4ff);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

}

nav{

display:flex;
gap:28px;

}

nav a{

text-decoration:none;

font-weight:600;

color:#333;

transition:.3s;

}

nav a:hover{

color:var(--primary);

}

/* ---------------------------- */

.hero{

height:100vh;

display:flex;

justify-content:center;

align-items:center;

text-align:center;

flex-direction:column;

padding:20px;

background:

linear-gradient(

rgba(0,0,0,.55),

rgba(0,0,0,.55)

),

url("https://images.unsplash.com/photo-1586773860418-d37222d8fce3?auto=format&fit=crop&w=1800&q=80");

background-size:cover;

background-position:center;

color:white;

}

.hero h1{

font-size:74px;

font-weight:800;

}

.hero p{

font-size:22px;

margin-top:20px;

max-width:900px;

line-height:1.8;

}

.heroButtons{

margin-top:40px;

display:flex;

gap:25px;

flex-wrap:wrap;

justify-content:center;

}

.heroButtons button{

padding:18px 42px;

border:none;

border-radius:40px;

cursor:pointer;

font-size:18px;

font-weight:600;

transition:.35s;

}

.primary{

background:var(--primary);

color:white;

}

.secondary{

background:white;

color:var(--primary);

}

.heroButtons button:hover{

transform:translateY(-8px);

box-shadow:

0 12px 30px

rgba(0,0,0,.25);

}

@media(max-width:768px){

header{

padding:15px 20px;

flex-direction:column;

gap:15px;

}

nav{

flex-wrap:wrap;

justify-content:center;

}

.hero h1{

font-size:42px;

}

.hero p{

font-size:17px;

}

}

</style>

</head>

<body>

<div class="loader">

<span></span>

</div>

<header>

<div class="logo">

🏥 CarePlus AI

</div>

<nav>

<a href="#">Home</a>

<a href="#about">About</a>

<a href="#departments">Departments</a>

<a href="#doctors">Doctors</a>

<a href="#appointment">Appointment</a>

<a href="#contact">Contact</a>

</nav>

</header>

<section class="hero">

<h1>

Future of Smart Healthcare

</h1>

<p>

AI-powered healthcare with world-class doctors, emergency support,
digital medical records, intelligent diagnosis assistance,
and premium patient care.

</p>

<div class="heroButtons">

<button class="primary">

Book Appointment

</button>

<button class="secondary">

Emergency

</button>

</div>

</section>

<!-- ================= ABOUT ================= -->

<section id="about" class="about">

<div class="aboutLeft">

<h2>About CarePlus AI Hospital</h2>

<p>

CarePlus AI Hospital is a next-generation healthcare platform that combines
experienced doctors, Artificial Intelligence, emergency care, digital medical
records, online appointments, and smart health monitoring to provide the best
patient experience.

</p>

<div class="features">

<div class="feature">

<i class="fa-solid fa-user-doctor"></i>

<h3>120+ Doctors</h3>

</div>

<div class="feature">

<i class="fa-solid fa-bed-pulse"></i>

<h3>500 Beds</h3>

</div>

<div class="feature">

<i class="fa-solid fa-ambulance"></i>

<h3>24×7 Emergency</h3>

</div>

<div class="feature">

<i class="fa-solid fa-heart-pulse"></i>

<h3>AI Diagnosis</h3>

</div>

</div>

</div>

<div class="aboutRight">

<img
src="https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=900&q=80">

</div>

</section>

<!-- ================= STATS ================= -->

<section class="stats">

<div class="stat">

<h1 id="patientCount">0</h1>

<p>Patients</p>

</div>

<div class="stat">

<h1 id="doctorCount">0</h1>

<p>Doctors</p>

</div>

<div class="stat">

<h1 id="operationCount">0</h1>

<p>Operations</p>

</div>

<div class="stat">

<h1 id="awardCount">0</h1>

<p>Awards</p>

</div>

</section>

<style>

.about{

display:grid;

grid-template-columns:1fr 1fr;

gap:50px;

padding:100px 8%;

align-items:center;

}

.about img{

width:100%;

border-radius:25px;

box-shadow:0 20px 40px rgba(0,0,0,.15);

}

.about h2{

font-size:42px;

margin-bottom:20px;

color:#0077ff;

}

.about p{

font-size:18px;

line-height:1.8;

margin-bottom:35px;

}

.features{

display:grid;

grid-template-columns:repeat(2,1fr);

gap:20px;

}

.feature{

background:white;

padding:25px;

border-radius:20px;

text-align:center;

box-shadow:0 10px 25px rgba(0,0,0,.08);

transition:.3s;

}

.feature:hover{

transform:translateY(-10px);

}

.feature i{

font-size:45px;

color:#0077ff;

margin-bottom:15px;

}

.stats{

display:grid;

grid-template-columns:repeat(4,1fr);

padding:70px;

background:linear-gradient(45deg,#0077ff,#00b4ff);

color:white;

text-align:center;

}

.stat h1{

font-size:58px;

}

.stat p{

font-size:20px;

margin-top:10px;

}

@media(max-width:900px){

.about{

grid-template-columns:1fr;

}

.stats{

grid-template-columns:repeat(2,1fr);

gap:30px;

}

}

</style>

<script>

function counter(id,target){

let x=0;

let timer=setInterval(function(){

x+=Math.ceil(target/100);

if(x>=target){

x=target;

clearInterval(timer);

}

document.getElementById(id).innerHTML=x.toLocaleString();

},20);

}

counter("patientCount",25000);

counter("doctorCount",120);

counter("operationCount",18000);

counter("awardCount",85);

</script>
<!-- ================= DEPARTMENTS ================= -->

<section id="departments" class="departments">

<h2 class="title">

Our Departments

</h2>

<div class="departmentGrid">

<div class="departmentCard">

<i class="fa-solid fa-heart-pulse"></i>

<h3>Cardiology</h3>

<p>

Advanced heart care with AI-assisted diagnosis.

</p>

</div>

<div class="departmentCard">

<i class="fa-solid fa-brain"></i>

<h3>Neurology</h3>

<p>

Expert treatment for brain and nervous system disorders.

</p>

</div>

<div class="departmentCard">

<i class="fa-solid fa-bone"></i>

<h3>Orthopedics</h3>

<p>

Bone, joint, and sports injury specialists.

</p>

</div>

<div class="departmentCard">

<i class="fa-solid fa-baby"></i>

<h3>Pediatrics</h3>

<p>

Complete healthcare for infants and children.

</p>

</div>

<div class="departmentCard">

<i class="fa-solid fa-eye"></i>

<h3>Ophthalmology</h3>

<p>

Eye care, laser treatment, and vision correction.

</p>

</div>

<div class="departmentCard">

<i class="fa-solid fa-tooth"></i>

<h3>Dental Care</h3>

<p>

Cosmetic and preventive dental treatment.

</p>

</div>

</div>

</section>

<!-- ================= SERVICES ================= -->

<section class="services">

<h2 class="title">

Hospital Services

</h2>

<div class="serviceGrid">

<div class="serviceCard">

<i class="fa-solid fa-robot"></i>

<h3>AI Receptionist</h3>

<p>

24×7 intelligent virtual receptionist.

</p>

</div>

<div class="serviceCard">

<i class="fa-solid fa-calendar-check"></i>

<h3>Appointments</h3>

<p>

Book appointments online anytime.

</p>

</div>

<div class="serviceCard">

<i class="fa-solid fa-truck-medical"></i>

<h3>Emergency</h3>

<p>

Rapid ambulance response system.

</p>

</div>

<div class="serviceCard">

<i class="fa-solid fa-flask"></i>

<h3>Laboratory</h3>

<p>

Modern diagnostic laboratory facilities.

</p>

</div>

<div class="serviceCard">

<i class="fa-solid fa-pills"></i>

<h3>Pharmacy</h3>

<p>

24-hour medicine availability.

</p>

</div>

<div class="serviceCard">

<i class="fa-solid fa-video"></i>

<h3>Video Consultation</h3>

<p>

Consult doctors from anywhere.

</p>

</div>

</div>

</section>

<style>

.title{

text-align:center;

font-size:42px;

margin-bottom:50px;

color:#0077ff;

}

.departments,
.services{

padding:100px 8%;

}

.departmentGrid,
.serviceGrid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(260px,1fr));

gap:30px;

}

.departmentCard,
.serviceCard{

background:white;

padding:35px;

border-radius:22px;

text-align:center;

box-shadow:0 12px 30px rgba(0,0,0,.08);

transition:.35s;

}

.departmentCard:hover,
.serviceCard:hover{

transform:translateY(-12px);

box-shadow:0 20px 40px rgba(0,0,0,.12);

}

.departmentCard i,
.serviceCard i{

font-size:55px;

color:#0077ff;

margin-bottom:20px;

}

.departmentCard h3,
.serviceCard h3{

margin-bottom:15px;

font-size:24px;

}

.departmentCard p,
.serviceCard p{

line-height:1.7;

color:#555;

}

</style>

<!-- ================= DOCTORS ================= -->

<section id="doctors" class="doctors">

<h2 class="title">

Meet Our Specialists

</h2>

<div class="doctorGrid">

<div class="doctor">

<img src="https://randomuser.me/api/portraits/men/32.jpg">

<h3>Dr. James Wilson</h3>

<p>Cardiologist</p>

<button>View Profile</button>

</div>

<div class="doctor">

<img src="https://randomuser.me/api/portraits/women/44.jpg">

<h3>Dr. Sarah Lee</h3>

<p>Neurologist</p>

<button>View Profile</button>

</div>

<div class="doctor">

<img src="https://randomuser.me/api/portraits/men/75.jpg">

<h3>Dr. David Smith</h3>

<p>Orthopedic</p>

<button>View Profile</button>

</div>

<div class="doctor">

<img src="https://randomuser.me/api/portraits/women/62.jpg">

<h3>Dr. Emily Clark</h3>

<p>Pediatrician</p>

<button>View Profile</button>

</div>

</div>

</section>

<!-- ================= REVIEWS ================= -->

<section class="reviews">

<h2 class="title">

Patient Reviews

</h2>

<div class="reviewContainer">

<div class="review">

⭐⭐⭐⭐⭐

<p>

Excellent doctors and very friendly staff.

</p>

<h4>- Mohamed</h4>

</div>

<div class="review">

⭐⭐⭐⭐⭐

<p>

Emergency service was very fast.

</p>

<h4>- Aisha</h4>

</div>

<div class="review">

⭐⭐⭐⭐⭐

<p>

Very clean hospital with modern equipment.

</p>

<h4>- Rahul</h4>

</div>

</div>

</section>

<!-- ================= GALLERY ================= -->

<section class="gallery">

<h2 class="title">

Hospital Gallery

</h2>

<div class="galleryGrid">

<img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=900&q=80">

<img src="https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=900&q=80">

<img src="https://images.unsplash.com/photo-1581056771107-24ca5f033842?auto=format&fit=crop&w=900&q=80">

<img src="https://images.unsplash.com/photo-1586773860418-d37222d8fce3?auto=format&fit=crop&w=900&q=80">

</div>

</section>

<style>

.doctors{

padding:100px 8%;

}

.doctorGrid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(260px,1fr));

gap:30px;

}

.doctor{

background:white;

padding:25px;

border-radius:20px;

text-align:center;

box-shadow:0 15px 30px rgba(0,0,0,.08);

transition:.4s;

}

.doctor:hover{

transform:translateY(-10px);

}

.doctor img{

width:150px;

height:150px;

border-radius:50%;

object-fit:cover;

margin-bottom:20px;

}

.doctor button{

margin-top:15px;

padding:12px 25px;

background:#0077ff;

color:white;

border:none;

border-radius:30px;

cursor:pointer;

}

.reviews{

padding:100px 8%;

background:#f8fbff;

}

.reviewContainer{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(300px,1fr));

gap:30px;

}

.review{

background:white;

padding:30px;

border-radius:20px;

box-shadow:0 10px 25px rgba(0,0,0,.08);

}

.gallery{

padding:100px 8%;

}

.galleryGrid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(260px,1fr));

gap:20px;

}

.galleryGrid img{

width:100%;

height:260px;

object-fit:cover;

border-radius:18px;

transition:.4s;

}

.galleryGrid img:hover{

transform:scale(1.05);

}

</style>

<!-- ================= CONTACT ================= -->

<section id="contact" class="contact">

<h2 class="title">

Contact Us

</h2>

<div class="contactContainer">

<div class="contactInfo">

<h3>CarePlus AI Hospital</h3>

<p>

📍 123 Health Street, Chennai, India

</p>

<p>

📞 +91 98765 43210

</p>

<p>

✉ careplus@example.com

</p>

<p>

🕒 Open 24 Hours

</p>

</div>

<div class="contactForm">

<input
type="text"
placeholder="Your Name">

<input
type="email"
placeholder="Email">

<textarea
placeholder="Your Message"></textarea>

<button>

Send Message

</button>

</div>

</div>

</section>

<!-- ================= MAP ================= -->

<section class="mapSection">

<h2 class="title">

Find Us

</h2>

<iframe

src="https://www.google.com/maps?q=Chennai&output=embed"

loading="lazy"

allowfullscreen>

</iframe>

</section>

<!-- ================= FOOTER ================= -->

<footer>

<div class="footerGrid">

<div>

<h3>CarePlus AI Hospital</h3>

<p>

Modern healthcare powered by Artificial Intelligence.

</p>

</div>

<div>

<h3>Quick Links</h3>

<ul>

<li>Home</li>

<li>Doctors</li>

<li>Departments</li>

<li>Appointments</li>

<li>Contact</li>

</ul>

</div>

<div>

<h3>Emergency</h3>

<p>

🚑 108

</p>

<p>

☎ +91 98765 43210

</p>

</div>

</div>

<p class="copyright">

© 2026 CarePlus AI Hospital

</p>

</footer>

<button id="topButton">

↑

</button>

<button id="darkButton">

🌙

</button>

<style>

.contact{

padding:100px 8%;

}

.contactContainer{

display:grid;

grid-template-columns:1fr 1fr;

gap:40px;

}

.contactInfo{

background:white;

padding:35px;

border-radius:20px;

box-shadow:0 12px 25px rgba(0,0,0,.08);

}

.contactInfo p{

margin:15px 0;

}

.contactForm{

display:grid;

gap:18px;

}

.contactForm input,
.contactForm textarea{

padding:18px;

border-radius:15px;

border:1px solid #ddd;

font-size:16px;

}

.contactForm textarea{

height:180px;

resize:none;

}

.contactForm button{

padding:18px;

border:none;

background:#0077ff;

color:white;

font-size:18px;

border-radius:40px;

cursor:pointer;

}

.mapSection{

padding:80px 8%;

}

.mapSection iframe{

width:100%;

height:420px;

border:none;

border-radius:25px;

}

footer{

background:#0f172a;

color:white;

padding:70px 8%;

margin-top:60px;

}

.footerGrid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(250px,1fr));

gap:35px;

margin-bottom:40px;

}

.footerGrid ul{

list-style:none;

}

.footerGrid li{

margin:10px 0;

}

.copyright{

text-align:center;

opacity:.8;

}

#topButton{

position:fixed;

right:30px;

bottom:30px;

width:60px;

height:60px;

border:none;

border-radius:50%;

background:#0077ff;

color:white;

font-size:24px;

cursor:pointer;

display:none;

z-index:999;

}

#darkButton{

position:fixed;

right:30px;

bottom:105px;

width:60px;

height:60px;

border:none;

border-radius:50%;

background:#111;

color:white;

font-size:22px;

cursor:pointer;

z-index:999;

}

.dark{

background:#111827;

color:white;

}

.dark header{

background:rgba(15,23,42,.92);

}

.dark .departmentCard,
.dark .serviceCard,
.dark .doctor,
.dark .feature,
.dark .review,
.dark .contactInfo{

background:#1f2937;

color:white;

}

@media(max-width:900px){

.contactContainer{

grid-template-columns:1fr;

}

}

</style>

<script>

const topBtn=document.getElementById("topButton");

window.onscroll=function(){

if(document.documentElement.scrollTop>300){

topBtn.style.display="block";

}else{

topBtn.style.display="none";

}

};

topBtn.onclick=function(){

window.scrollTo({

top:0,

behavior:"smooth"

});

};

document

.getElementById("darkButton")

.onclick=function(){

document.body.classList.toggle("dark");

};

</script>
<!-- ================= CONTACT ================= -->

<section id="contact" class="contact">

<h2 class="title">Contact CarePlus AI Hospital</h2>

<div class="contactGrid">

<div class="contactCard">

<h3>Hospital Information</h3>

<p>📍 Chennai, Tamil Nadu, India</p>

<p>☎ +91 9876543210</p>

<p>✉ support@careplus.ai</p>

<p>🕒 24 × 7 Emergency Service</p>

<div class="socialIcons">

<i class="fab fa-facebook"></i>

<i class="fab fa-instagram"></i>

<i class="fab fa-linkedin"></i>

<i class="fab fa-youtube"></i>

</div>

</div>

<div class="contactCard">

<input
type="text"
placeholder="Full Name">

<input
type="email"
placeholder="Email">

<input
type="tel"
placeholder="Phone">

<textarea
placeholder="Your Message"></textarea>

<button>

Send Message

</button>

</div>

</div>

</section>

<!-- ================= GOOGLE MAP ================= -->

<section class="mapSection">

<h2 class="title">

Hospital Location

</h2>

<iframe

src="https://www.google.com/maps?q=Chennai&output=embed"

loading="lazy">

</iframe>

</section>

<!-- ================= FOOTER ================= -->

<footer>

<div class="footerGrid">

<div>

<h2>🏥 CarePlus AI</h2>

<p>

Premium Smart Hospital powered by Artificial Intelligence.

</p>

</div>

<div>

<h3>Quick Links</h3>

<ul>

<li>Home</li>

<li>Doctors</li>

<li>Departments</li>

<li>Gallery</li>

<li>Contact</li>

</ul>

</div>

<div>

<h3>Emergency</h3>

<p>🚑 108</p>

<p>☎ +91 9876543210</p>

</div>

</div>

<hr>

<p class="copyright">

© 2026 CarePlus AI Hospital

</p>

</footer>

<button id="topBtn">

↑

</button>

<button id="themeBtn">

🌙

</button>

<style>

.contact{

padding:90px 8%;

}

.contactGrid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(350px,1fr));

gap:40px;

}

.contactCard{

background:white;

padding:35px;

border-radius:20px;

box-shadow:0 15px 35px rgba(0,0,0,.08);

}

.contactCard input,
.contactCard textarea{

width:100%;

padding:16px;

margin-bottom:15px;

border:1px solid #ddd;

border-radius:12px;

font-size:16px;

}

.contactCard textarea{

height:150px;

resize:none;

}

.contactCard button{

width:100%;

padding:16px;

background:#0077ff;

color:white;

border:none;

border-radius:12px;

cursor:pointer;

font-size:17px;

}

.socialIcons{

margin-top:20px;

display:flex;

gap:20px;

font-size:28px;

color:#0077ff;

}

.mapSection{

padding:80px 8%;

}

.mapSection iframe{

width:100%;

height:420px;

border:none;

border-radius:20px;

}

footer{

background:#071320;

color:white;

padding:70px 8%;

margin-top:60px;

}

.footerGrid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(250px,1fr));

gap:30px;

}

.footerGrid ul{

list-style:none;

}

.footerGrid li{

margin:10px 0;

}

footer hr{

margin:40px 0;

opacity:.2;

}

.copyright{

text-align:center;

}

#topBtn{

position:fixed;

right:25px;

bottom:25px;

width:60px;

height:60px;

border:none;

border-radius:50%;

background:#0077ff;

color:white;

font-size:24px;

cursor:pointer;

display:none;

z-index:999;

}

#themeBtn{

position:fixed;

right:25px;

bottom:100px;

width:60px;

height:60px;

border:none;

border-radius:50%;

background:#111;

color:white;

font-size:22px;

cursor:pointer;

z-index:999;

}

.darkMode{

background:#111827;

color:white;

}

.darkMode .contactCard,
.darkMode .doctor,
.darkMode .departmentCard,
.darkMode .serviceCard,
.darkMode .review{

background:#1f2937;

color:white;

}

</style>

<script>

const topBtn=document.getElementById("topBtn");

window.addEventListener("scroll",function(){

if(window.scrollY>300){

topBtn.style.display="block";

}else{

topBtn.style.display="none";

}

});

topBtn.onclick=function(){

window.scrollTo({

top:0,

behavior:"smooth"

});

};

document.getElementById("themeBtn").onclick=function(){

document.body.classList.toggle("darkMode");

};

</script>
<!-- ================= AI MODULE ================= -->

<section id="ai-center" class="ai-center">

<h2 class="title">🤖 CarePlus AI Assistant</h2>

<p class="subtitle">
Talk with our AI Receptionist or check your symptoms.
</p>

<div class="ai-grid">

<div class="ai-card">

<div class="robot-avatar">
🤖
</div>

<h3>AI Receptionist</h3>

<p id="robotText">

Hello 👋 Welcome to CarePlus AI Hospital.

</p>

<button onclick="robotSpeak()">

🎤 Speak

</button>

</div>

<div class="ai-card">

<h3>AI Symptom Checker</h3>

<textarea

id="symptom"

placeholder="Example: fever, cough, headache">

</textarea>

<button onclick="checkSymptoms()">

Analyze

</button>

<p id="symptomResult">

</p>

</div>

</div>

</section>

<section class="chatbot">

<h2 class="title">

💬 AI Chatbot

</h2>

<div id="chatBox" class="chatBox">

<div class="bot">

Hello 👋

Ask me about:

<ul>

<li>Doctors</li>

<li>Appointments</li>

<li>Emergency</li>

<li>Departments</li>

</ul>

</div>

</div>

<div class="chatInput">

<input

type="text"

id="message"

placeholder="Type your message">

<button

onclick="chatSend()">

Send

</button>

</div>

</section>

<style>

.ai-center{

padding:90px 8%;

background:#f8fbff;

}

.subtitle{

text-align:center;

margin-bottom:40px;

}

.ai-grid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(340px,1fr));

gap:35px;

}

.ai-card{

background:white;

padding:30px;

border-radius:22px;

box-shadow:0 15px 35px rgba(0,0,0,.08);

text-align:center;

}

.robot-avatar{

font-size:90px;

animation:floatRobot 3s infinite;

}

.ai-card textarea{

width:100%;

height:160px;

padding:15px;

margin:20px 0;

border-radius:12px;

border:1px solid #ccc;

resize:none;

}

.ai-card button{

padding:15px 35px;

border:none;

border-radius:35px;

background:#0077ff;

color:white;

cursor:pointer;

}

.chatbot{

padding:90px 8%;

}

.chatBox{

height:350px;

overflow-y:auto;

background:white;

padding:20px;

border-radius:20px;

box-shadow:0 10px 30px rgba(0,0,0,.08);

}

.bot{

background:#eef7ff;

padding:15px;

border-radius:15px;

margin-bottom:15px;

}

.user{

background:#0077ff;

color:white;

padding:15px;

border-radius:15px;

margin:15px 0;

text-align:right;

}

.chatInput{

display:flex;

gap:15px;

margin-top:20px;

}

.chatInput input{

flex:1;

padding:18px;

border-radius:12px;

border:1px solid #ccc;

}

.chatInput button{

padding:18px 35px;

border:none;

background:#0077ff;

color:white;

border-radius:12px;

cursor:pointer;

}

@keyframes floatRobot{

50%{

transform:translateY(-12px);

}

}

</style>

<script>

function robotSpeak(){

const speech=new SpeechSynthesisUtterance(

"Welcome to Care Plus AI Hospital. How may I help you today?"

);

speechSynthesis.speak(speech);

}

function checkSymptoms(){

let value=document

.getElementById("symptom")

.value

.toLowerCase();

let result="Please consult our doctor.";

if(value.includes("fever"))

result="Possible viral infection.";

else if(value.includes("cough"))

result="Possible respiratory illness.";

else if(value.includes("head"))

result="Possible migraine.";

else if(value.includes("chest"))

result="Emergency! Visit the Emergency Department immediately.";

document

.getElementById("symptomResult")

.innerHTML=result;

}

function chatSend(){

let input=document

.getElementById("message");

let text=input.value.trim();

if(text=="") return;

let box=document

.getElementById("chatBox");

box.innerHTML+=

'<div class="user">'+text+'</div>';

let reply="Please visit our reception desk.";

let q=text.toLowerCase();

if(q.includes("appointment"))

reply="Appointments are available from 9 AM to 8 PM.";

else if(q.includes("doctor"))

reply="We have over 120 specialist doctors.";

else if(q.includes("emergency"))

reply="Emergency ambulance is available 24×7.";

else if(q.includes("blood"))

reply="Our blood bank is open all day.";

else if(q.includes("cardiology"))

reply="Cardiology Department is on Floor 2.";

box.innerHTML+=

'<div class="bot">'+reply+'</div>';

box.scrollTop=box.scrollHeight;

input.value="";

}

</script>
<!-- ================= APPOINTMENT ================= -->

<section id="appointment" class="appointmentSection">

<h2 class="title">

📅 Smart Appointment Booking

</h2>

<div class="appointmentGrid">

<div class="appointmentCard">

<input
type="text"
id="patientName"
placeholder="Patient Name">

<input
type="email"
id="patientEmail"
placeholder="Email">

<input
type="tel"
id="patientPhone"
placeholder="Phone Number">

<select id="department">

<option>Cardiology</option>

<option>Neurology</option>

<option>Orthopedics</option>

<option>Pediatrics</option>

<option>Dermatology</option>

<option>ENT</option>

</select>

<input
type="date"
id="appointmentDate">

<select id="appointmentTime">

<option>09:00 AM</option>

<option>10:00 AM</option>

<option>11:00 AM</option>

<option>12:00 PM</option>

<option>02:00 PM</option>

<option>03:00 PM</option>

<option>04:00 PM</option>

</select>

<button onclick="bookAppointment()">

Book Appointment

</button>

<p id="appointmentStatus"></p>

</div>

<div class="doctorSearchCard">

<h3>

👨‍⚕️ Doctor Search

</h3>

<input

type="text"

id="doctorSearch"

placeholder="Search Doctor">

<div id="doctorResults">

<div class="doctorItem">

Dr. James Wilson — Cardiology

</div>

<div class="doctorItem">

Dr. Sarah Lee — Neurology

</div>

<div class="doctorItem">

Dr. David Smith — Orthopedics

</div>

<div class="doctorItem">

Dr. Emily Clark — Pediatrics

</div>

</div>

</div>

</div>

</section>

<style>

.appointmentSection{

padding:90px 8%;

background:#f6fbff;

}

.appointmentGrid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(350px,1fr));

gap:35px;

}

.appointmentCard,
.doctorSearchCard{

background:white;

padding:30px;

border-radius:20px;

box-shadow:0 15px 30px rgba(0,0,0,.08);

}

.appointmentCard input,
.appointmentCard select,
.doctorSearchCard input{

width:100%;

padding:15px;

margin-bottom:15px;

border:1px solid #ddd;

border-radius:12px;

font-size:16px;

}

.appointmentCard button{

width:100%;

padding:16px;

border:none;

background:#0077ff;

color:white;

font-size:18px;

border-radius:12px;

cursor:pointer;

}

#appointmentStatus{

margin-top:18px;

font-weight:bold;

color:green;

}

.doctorItem{

padding:15px;

margin-top:12px;

background:#eef7ff;

border-radius:10px;

transition:.3s;

}

.doctorItem:hover{

background:#d9ecff;

}

</style>

<script>

function bookAppointment(){

let name=document.getElementById("patientName").value;

let dept=document.getElementById("department").value;

let date=document.getElementById("appointmentDate").value;

let time=document.getElementById("appointmentTime").value;

if(name===""){

document.getElementById("appointmentStatus").innerHTML=

"Please enter your name.";

return;

}

document.getElementById("appointmentStatus").innerHTML=

"✅ Appointment booked for "+name+
"<br>"+dept+
"<br>"+date+
"<br>"+time;

}

const search=document.getElementById("doctorSearch");

search.addEventListener("keyup",function(){

let filter=this.value.toLowerCase();

let doctors=document.querySelectorAll(".doctorItem");

doctors.forEach(function(item){

if(item.innerText.toLowerCase().includes(filter)){

item.style.display="block";

}else{

item.style.display="none";

}

});

});

</script>
<!-- ================= LOGIN PORTAL ================= -->

<section id="loginPortal" class="loginPortal">

<h2 class="title">

🔐 Hospital Login Portal

</h2>

<div class="loginGrid">

<div class="loginCard">

<div class="icon">

👤

</div>

<h3>

Patient Login

</h3>

<input
type="text"
placeholder="Patient ID">

<input
type="password"
placeholder="Password">

<button onclick="patientLogin()">

Login

</button>

<p id="patientStatus"></p>

</div>

<div class="loginCard">

<div class="icon">

🩺

</div>

<h3>

Doctor Login

</h3>

<input
type="text"
placeholder="Doctor ID">

<input
type="password"
placeholder="Password">

<button onclick="doctorLogin()">

Login

</button>

<p id="doctorStatus"></p>

</div>

<div class="loginCard">

<div class="icon">

🛡️

</div>

<h3>

Admin Login

</h3>

<input
type="text"
placeholder="Admin ID">

<input
type="password"
placeholder="Password">

<button onclick="adminLogin()">

Login

</button>

<p id="adminStatus"></p>

</div>

</div>

</section>

<!-- ================= DASHBOARD ================= -->

<section class="dashboard">

<h2 class="title">

📊 Patient Dashboard Preview

</h2>

<div class="dashboardGrid">

<div class="dashboardCard">

<h3>

Appointments

</h3>

<h1>

12

</h1>

</div>

<div class="dashboardCard">

<h3>

Reports

</h3>

<h1>

28

</h1>

</div>

<div class="dashboardCard">

<h3>

Prescriptions

</h3>

<h1>

9

</h1>

</div>

<div class="dashboardCard">

<h3>

BMI

</h3>

<h1>

23.5

</h1>

</div>

</div>

</section>

<!-- ================= MEDICAL RECORDS ================= -->

<section class="records">

<h2 class="title">

📂 Medical Records

</h2>

<table>

<tr>

<th>Date</th>

<th>Department</th>

<th>Doctor</th>

<th>Status</th>

</tr>

<tr>

<td>10-07-2026</td>

<td>Cardiology</td>

<td>Dr. James</td>

<td>Completed</td>

</tr>

<tr>

<td>18-07-2026</td>

<td>Neurology</td>

<td>Dr. Sarah</td>

<td>Follow-up</td>

</tr>

<tr>

<td>25-07-2026</td>

<td>Orthopedics</td>

<td>Dr. David</td>

<td>Completed</td>

</tr>

</table>

</section>

<style>

.loginPortal{

padding:90px 8%;

background:#f5fbff;

}

.loginGrid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(300px,1fr));

gap:30px;

}

.loginCard{

background:white;

padding:30px;

border-radius:20px;

text-align:center;

box-shadow:0 15px 30px rgba(0,0,0,.08);

transition:.35s;

}

.loginCard:hover{

transform:translateY(-10px);

}

.icon{

font-size:70px;

margin-bottom:15px;

}

.loginCard input{

width:100%;

padding:15px;

margin:10px 0;

border-radius:10px;

border:1px solid #ccc;

}

.loginCard button{

width:100%;

padding:15px;

border:none;

background:#0077ff;

color:white;

font-size:17px;

border-radius:10px;

cursor:pointer;

}

.dashboard{

padding:90px 8%;

}

.dashboardGrid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:25px;

}

.dashboardCard{

background:white;

padding:30px;

border-radius:20px;

text-align:center;

box-shadow:0 12px 25px rgba(0,0,0,.08);

}

.dashboardCard h1{

font-size:55px;

color:#0077ff;

margin-top:15px;

}

.records{

padding:90px 8%;

}

.records table{

width:100%;

border-collapse:collapse;

background:white;

box-shadow:0 12px 25px rgba(0,0,0,.08);

}

.records th{

background:#0077ff;

color:white;

padding:18px;

}

.records td{

padding:18px;

border-bottom:1px solid #eee;

}

</style>

<script>

function patientLogin(){

document

.getElementById("patientStatus")

.innerHTML="✅ Patient Login Successful";

}

function doctorLogin(){

document

.getElementById("doctorStatus")

.innerHTML="✅ Doctor Login Successful";

}

function adminLogin(){

document

.getElementById("adminStatus")

.innerHTML="✅ Admin Login Successful";

}

</script>
<!-- ================= PART 2D ================= -->

<section id="emergency" class="emergencySection">

<h2 class="title">

🚑 Emergency & Blood Bank

</h2>

<div class="emergencyGrid">

<div class="emergencyCard">

<h3>Blood Bank</h3>

<table class="bloodTable">

<tr>
<th>Blood</th>
<th>Units</th>
</tr>

<tr><td>A+</td><td id="aPos">24</td></tr>
<tr><td>A-</td><td>8</td></tr>
<tr><td>B+</td><td>16</td></tr>
<tr><td>B-</td><td>5</td></tr>
<tr><td>O+</td><td>41</td></tr>
<tr><td>O-</td><td>7</td></tr>
<tr><td>AB+</td><td>10</td></tr>
<tr><td>AB-</td><td>3</td></tr>

</table>

<button onclick="requestBlood()">

Request Blood

</button>

<p id="bloodStatus"></p>

</div>

<div class="emergencyCard">

<h3>Book Ambulance</h3>

<input
type="text"
id="location"
placeholder="Current Location">

<input
type="text"
id="patient"
placeholder="Patient Name">

<select id="priority">

<option>Normal</option>
<option>Urgent</option>
<option>Critical</option>

</select>

<button onclick="bookAmbulance()">

Call Ambulance

</button>

<p id="ambulanceStatus"></p>

</div>

</div>

</section>

<section class="healthTools">

<h2 class="title">

❤️ BMI Calculator

</h2>

<div class="bmiBox">

<input
type="number"
id="height"
placeholder="Height (cm)">

<input
type="number"
id="weight"
placeholder="Weight (kg)">

<button onclick="calculateBMI()">

Calculate BMI

</button>

<h3 id="bmiResult"></h3>

</div>

</section>

<section class="ecgSection">

<h2 class="title">

Live ECG Monitor

</h2>

<div class="ecg">

<div class="wave"></div>

</div>

</section>

<section class="utilities">

<button onclick="changeLanguage()">

🌍 Language

</button>

<button onclick="voiceCommand()">

🎤 Voice Command

</button>

</section>

<style>

.emergencySection{

padding:90px 8%;

background:#f8fbff;

}

.emergencyGrid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(350px,1fr));

gap:30px;

}

.emergencyCard{

background:white;

padding:30px;

border-radius:20px;

box-shadow:0 12px 30px rgba(0,0,0,.08);

}

.emergencyCard input,
.emergencyCard select{

width:100%;

padding:14px;

margin:10px 0;

border:1px solid #ddd;

border-radius:10px;

}

.emergencyCard button{

width:100%;

padding:15px;

background:#0077ff;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

}

.bloodTable{

width:100%;

border-collapse:collapse;

margin:20px 0;

}

.bloodTable th,
.bloodTable td{

padding:12px;

border:1px solid #ddd;

text-align:center;

}

.healthTools{

padding:90px 8%;

text-align:center;

}

.bmiBox{

max-width:450px;

margin:auto;

background:white;

padding:30px;

border-radius:20px;

box-shadow:0 12px 25px rgba(0,0,0,.08);

}

.bmiBox input{

width:100%;

padding:15px;

margin:12px 0;

border-radius:10px;

border:1px solid #ccc;

}

.bmiBox button{

width:100%;

padding:15px;

background:#00a651;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

}

.ecgSection{

padding:80px 8%;

background:#111;

color:white;

text-align:center;

}

.ecg{

width:100%;

height:140px;

overflow:hidden;

position:relative;

}

.wave{

position:absolute;

top:60px;

left:0;

width:300%;

height:4px;

background:#00ff66;

animation:moveECG 4s linear infinite;

clip-path:polygon(
0 50%,
8% 50%,
10% 20%,
12% 80%,
14% 0,
16% 100%,
20% 50%,
100% 50%
);

}

.utilities{

padding:70px;

display:flex;

justify-content:center;

gap:20px;

flex-wrap:wrap;

}

.utilities button{

padding:16px 35px;

background:#0077ff;

color:white;

border:none;

border-radius:35px;

cursor:pointer;

}

@keyframes moveECG{

100%{

transform:translateX(-50%);

}

}

</style>

<script>

function requestBlood(){

document.getElementById("bloodStatus").innerHTML=

"✅ Blood request submitted successfully.";

}

function bookAmbulance(){

let patient=document.getElementById("patient").value;

document.getElementById("ambulanceStatus").innerHTML=

"🚑 Ambulance dispatched for "+patient;

}

function calculateBMI(){

let h=document.getElementById("height").value/100;

let w=document.getElementById("weight").value;

if(!h || !w){

document.getElementById("bmiResult").innerHTML="Enter valid values";

return;

}

let bmi=(w/(h*h)).toFixed(1);

document.getElementById("bmiResult").innerHTML=

"Your BMI : "+bmi;

}

function changeLanguage(){

alert("Language switch demo.");

}

function voiceCommand(){

const speech=new SpeechSynthesisUtterance(

"Voice assistant activated."

);

speechSynthesis.speak(speech);

}

</script>

<!-- ================= PART 3 ================= -->

<section id="dashboard" class="dashboardSection">

<h2 class="title">

🏥 Smart Hospital Dashboard

</h2>

<div class="dashboardGrid">

<div class="dashboardBox">

<h3>

👤 Patient Dashboard

</h3>

<ul>

<li>✔ Upcoming Appointment</li>

<li>✔ Medical Reports</li>

<li>✔ Prescriptions</li>

<li>✔ AI Health Score</li>

</ul>

<button>

Open Dashboard

</button>

</div>

<div class="dashboardBox">

<h3>

👨‍⚕️ Doctor Dashboard

</h3>

<ul>

<li>✔ Today's Patients</li>

<li>✔ Appointments</li>

<li>✔ Surgery Schedule</li>

<li>✔ Medical Notes</li>

</ul>

<button>

Open Dashboard

</button>

</div>

<div class="dashboardBox">

<h3>

🛡 Admin Dashboard

</h3>

<ul>

<li>✔ Manage Doctors</li>

<li>✔ Manage Patients</li>

<li>✔ Manage Staff</li>

<li>✔ Hospital Reports</li>

</ul>

<button>

Open Dashboard

</button>

</div>

</div>

</section>

<section class="pharmacySection">

<h2 class="title">

💊 Smart Pharmacy

</h2>

<input

type="text"

id="medicineSearch"

placeholder="Search Medicine">

<div id="medicineList">

<div class="medicine">

Paracetamol

</div>

<div class="medicine">

Dolo 650

</div>

<div class="medicine">

Amoxicillin

</div>

<div class="medicine">

Vitamin C

</div>

<div class="medicine">

Crocin

</div>

<div class="medicine">

Insulin

</div>

</div>

</section>

<section class="liveStatus">

<h2 class="title">

📈 Live Hospital Status

</h2>

<div class="statusGrid">

<div class="statusCard">

<h1 id="bedCount">

186

</h1>

<p>

Available Beds

</p>

</div>

<div class="statusCard">

<h1 id="doctorOnline">

54

</h1>

<p>

Doctors Online

</p>

</div>

<div class="statusCard">

<h1 id="icuCount">

21

</h1>

<p>

ICU Beds

</p>

</div>

<div class="statusCard">

<h1 id="waiting">

13

</h1>

<p>

Patients Waiting

</p>

</div>

</div>

</section>

<style>

.dashboardSection{

padding:90px 8%;

background:#f8fbff;

}

.dashboardGrid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(300px,1fr));

gap:30px;

}

.dashboardBox{

background:white;

padding:30px;

border-radius:20px;

box-shadow:0 12px 30px rgba(0,0,0,.08);

transition:.3s;

}

.dashboardBox:hover{

transform:translateY(-10px);

}

.dashboardBox ul{

margin:20px 0;

padding-left:20px;

}

.dashboardBox li{

margin:12px 0;

}

.dashboardBox button{

width:100%;

padding:15px;

border:none;

background:#0077ff;

color:white;

border-radius:12px;

cursor:pointer;

}

.pharmacySection{

padding:90px 8%;

}

.pharmacySection input{

width:100%;

padding:18px;

border-radius:12px;

border:1px solid #ddd;

margin-bottom:25px;

}

.medicine{

padding:18px;

background:white;

margin-bottom:12px;

border-radius:12px;

box-shadow:0 8px 20px rgba(0,0,0,.06);

}

.liveStatus{

padding:90px 8%;

background:#eef8ff;

}

.statusGrid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:25px;

}

.statusCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 12px 25px rgba(0,0,0,.08);

}

.statusCard h1{

font-size:55px;

color:#0077ff;

margin-bottom:15px;

}

</style>

<script>

document.getElementById("medicineSearch")

.addEventListener("keyup",function(){

let value=this.value.toLowerCase();

let items=document.querySelectorAll(".medicine");

items.forEach(function(item){

if(item.innerText.toLowerCase().includes(value)){

item.style.display="block";

}else{

item.style.display="none";

}

});

});

setInterval(function(){

document.getElementById("waiting").innerHTML=

Math.floor(Math.random()*20)+5;

},5000);

</script>
<!-- ================= PART 4A ================= -->

<section id="aiReception" class="aiSection">

<h2 class="title">🤖 AI Receptionist</h2>

<div class="robotContainer">

<div class="robotHead">

<div class="eye leftEye"></div>

<div class="eye rightEye"></div>

<div class="mouth"></div>

</div>

<h3>CarePlus AI Assistant</h3>

<p id="robotText">

Hello 👋 Welcome to CarePlus Hospital.

</p>

<button onclick="robotSpeak()">

Talk to AI

</button>

<button onclick="toggleChat()">

Open Chat

</button>

</div>

</section>

<div class="chatBot" id="chatBox">

<div class="chatHeader">

AI Hospital Assistant

<span onclick="toggleChat()" class="closeBtn">✖</span>

</div>

<div id="chatMessages" class="chatMessages">

<div class="bot">

Hello! Ask me anything.

</div>

</div>

<div class="chatInput">

<input
type="text"
id="userMessage"
placeholder="Type your question...">

<button onclick="sendAIMessage()">

Send

</button>

</div>

</div>

<div id="notification" class="notification">

🏥 Welcome to CarePlus Hospital

</div>

<section class="announcement">

<marquee>

🚑 Emergency Service Available 24×7 |
💉 Blood Donation Camp on Sunday |
👨‍⚕️ Free Diabetes Checkup Tomorrow

</marquee>

</section>

<style>

.aiSection{

padding:90px 8%;

text-align:center;

background:#f7fbff;

}

.robotContainer{

max-width:420px;

margin:auto;

padding:35px;

background:white;

border-radius:25px;

box-shadow:0 15px 30px rgba(0,0,0,.1);

}

.robotHead{

width:170px;

height:170px;

background:#0077ff;

border-radius:50%;

margin:auto;

position:relative;

animation:floatRobot 3s infinite ease-in-out;

}

.eye{

width:22px;

height:22px;

background:white;

border-radius:50%;

position:absolute;

top:55px;

animation:blink 4s infinite;

}

.leftEye{

left:42px;

}

.rightEye{

right:42px;

}

.mouth{

width:65px;

height:8px;

background:white;

position:absolute;

bottom:45px;

left:52px;

border-radius:20px;

}

.robotContainer button{

margin:10px;

padding:15px 28px;

border:none;

border-radius:12px;

background:#0077ff;

color:white;

cursor:pointer;

}

.chatBot{

position:fixed;

bottom:30px;

right:30px;

width:340px;

background:white;

border-radius:20px;

box-shadow:0 12px 35px rgba(0,0,0,.2);

display:none;

overflow:hidden;

z-index:9999;

}

.chatHeader{

background:#0077ff;

color:white;

padding:16px;

font-weight:bold;

}

.closeBtn{

float:right;

cursor:pointer;

}

.chatMessages{

height:300px;

overflow-y:auto;

padding:15px;

background:#f9f9f9;

}

.bot{

background:#e8f2ff;

padding:12px;

border-radius:12px;

margin-bottom:10px;

}

.user{

background:#0077ff;

color:white;

padding:12px;

border-radius:12px;

margin-bottom:10px;

text-align:right;

}

.chatInput{

display:flex;

}

.chatInput input{

flex:1;

padding:15px;

border:none;

outline:none;

}

.chatInput button{

padding:15px;

border:none;

background:#0077ff;

color:white;

cursor:pointer;

}

.notification{

position:fixed;

top:25px;

right:25px;

background:#00a651;

color:white;

padding:16px 22px;

border-radius:10px;

display:none;

z-index:99999;

}

.announcement{

background:#0077ff;

color:white;

padding:12px;

font-weight:bold;

}

@keyframes floatRobot{

50%{

transform:translateY(-12px);

}

}

@keyframes blink{

0%,95%,100%{

transform:scaleY(1);

}

97%{

transform:scaleY(.1);

}

}

</style>

<script>

function robotSpeak(){

let text="Welcome to CarePlus Hospital. How can I help you today?";

document.getElementById("robotText").innerHTML=text;

speechSynthesis.speak(new SpeechSynthesisUtterance(text));

}

function toggleChat(){

let box=document.getElementById("chatBox");

box.style.display=(box.style.display==="block")?"none":"block";

}

function sendAIMessage(){

let input=document.getElementById("userMessage");

let msg=input.value.trim();

if(msg==="") return;

let area=document.getElementById("chatMessages");

area.innerHTML+="<div class='user'>"+msg+"</div>";

let reply="Please contact our reception.";

let m=msg.toLowerCase();

if(m.includes("doctor"))

reply="Doctors are available from 9 AM to 8 PM.";

else if(m.includes("appointment"))

reply="You can book appointments from the Appointment section.";

else if(m.includes("emergency"))

reply="Emergency services are available 24×7.";

else if(m.includes("blood"))

reply="Blood Bank is open all day.";

else if(m.includes("pharmacy"))

reply="Our pharmacy is open 24 hours.";

area.innerHTML+="<div class='bot'>"+reply+"</div>";

area.scrollTop=area.scrollHeight;

input.value="";

}

setTimeout(function(){

let n=document.getElementById("notification");

n.style.display="block";

setTimeout(function(){

n.style.display="none";

},5000);

},1500);

</script>
<!-- ================= PART 4B ================= -->

<section id="videoConsultation" class="videoConsultation">

<h2 class="title">🎥 Video Consultation</h2>

<div class="videoContainer">

<div class="videoScreen">

<video id="localVideo" autoplay playsinline muted></video>

<div class="videoPlaceholder" id="videoPlaceholder">

📹 Camera Preview

</div>

</div>

<div class="consultationPanel">

<h3>Doctor Consultation</h3>

<input type="text" id="patientNameVC" placeholder="Patient Name">

<select id="doctorVC">

<option>Choose Doctor</option>

<option>Dr. James Wilson - Cardiology</option>

<option>Dr. Sarah Lee - Neurology</option>

<option>Dr. David Smith - Orthopedics</option>

<option>Dr. Emily Clark - Pediatrics</option>

</select>

<textarea id="patientIssue"

placeholder="Describe your symptoms..."

rows="5"></textarea>

<div class="videoButtons">

<button onclick="startCamera()">📹 Start Camera</button>

<button onclick="stopCamera()">🛑 Stop Camera</button>

<button onclick="startConsultation()">📞 Join Call</button>

<button onclick="endConsultation()">❌ End Call</button>

</div>

<p id="consultationStatus"></p>

</div>

</div>

</section>

<style>

.videoConsultation{

padding:90px 8%;

background:#f5fbff;

}

.videoContainer{

display:grid;

grid-template-columns:2fr 1fr;

gap:30px;

}

.videoScreen{

background:#111;

height:500px;

border-radius:20px;

overflow:hidden;

position:relative;

display:flex;

align-items:center;

justify-content:center;

}

.videoScreen video{

width:100%;

height:100%;

object-fit:cover;

display:none;

}

.videoPlaceholder{

position:absolute;

font-size:32px;

color:white;

}

.consultationPanel{

background:white;

padding:30px;

border-radius:20px;

box-shadow:0 15px 30px rgba(0,0,0,.08);

}

.consultationPanel input,

.consultationPanel select,

.consultationPanel textarea{

width:100%;

padding:15px;

margin:12px 0;

border-radius:10px;

border:1px solid #ccc;

}

.videoButtons{

display:grid;

grid-template-columns:1fr 1fr;

gap:12px;

margin-top:20px;

}

.videoButtons button{

padding:14px;

background:#0077ff;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

}

.videoButtons button:hover{

background:#005ed8;

}

#consultationStatus{

margin-top:20px;

font-weight:bold;

color:#0077ff;

}

@media(max-width:900px){

.videoContainer{

grid-template-columns:1fr;

}

.videoScreen{

height:350px;

}

}

</style>

<script>

let localStream=null;

async function startCamera(){

try{

localStream=await navigator.mediaDevices.getUserMedia({

video:true,

audio:true

});

const video=document.getElementById("localVideo");

video.srcObject=localStream;

video.style.display="block";

document.getElementById("videoPlaceholder").style.display="none";

document.getElementById("consultationStatus").innerHTML=

"📹 Camera Started Successfully";

}

catch(e){

document.getElementById("consultationStatus").innerHTML=

"❌ Camera Permission Denied";

}

}

function stopCamera(){

if(localStream){

localStream.getTracks().forEach(track=>track.stop());

}

document.getElementById("localVideo").style.display="none";

document.getElementById("videoPlaceholder").style.display="flex";

document.getElementById("consultationStatus").innerHTML=

"🛑 Camera Stopped";

}

function startConsultation(){

let patient=document.getElementById("patientNameVC").value;

let doctor=document.getElementById("doctorVC").value;

if(patient===""){

alert("Enter Patient Name");

return;

}

document.getElementById("consultationStatus").innerHTML=

"📞 Connecting "+patient+" with "+doctor+" ...";

}

function endConsultation(){

document.getElementById("consultationStatus").innerHTML=

"❌ Consultation Ended";

stopCamera();

}

</script>
<!-- ================= PART 4C ================= -->

<section class="settingsSection">

<h2 class="title">⚙ Smart Settings</h2>

<div class="settingsGrid">

<div class="settingCard">

<h3>🌙 Dark Mode</h3>

<button onclick="toggleDarkMode()">

Enable / Disable

</button>

</div>

<div class="settingCard">

<h3>🌐 Language</h3>

<select id="languageSelect" onchange="changeLanguage()">

<option value="en">English</option>

<option value="ta">Tamil</option>

<option value="hi">Hindi</option>

<option value="ar">Arabic</option>

</select>

</div>

<div class="settingCard">

<h3>🔔 Notifications</h3>

<button onclick="showNotification()">

Show Notification

</button>

</div>

<div class="settingCard">

<h3>🎨 Theme Color</h3>

<input type="color"

id="themeColor"

value="#0077ff"

onchange="changeThemeColor()">

</div>

</div>

</section>

<canvas id="particlesCanvas"></canvas>

<div id="toast" class="toastMessage">

Welcome to CarePlus Hospital

</div>

<style>

.settingsSection{

padding:90px 8%;

background:#eef8ff;

}

.settingsGrid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(250px,1fr));

gap:25px;

}

.settingCard{

background:white;

padding:30px;

border-radius:20px;

text-align:center;

box-shadow:0 12px 30px rgba(0,0,0,.08);

}

.settingCard button,

.settingCard select,

.settingCard input{

margin-top:15px;

padding:12px;

width:100%;

border-radius:10px;

border:1px solid #ddd;

cursor:pointer;

}

#particlesCanvas{

position:fixed;

left:0;

top:0;

width:100%;

height:100%;

pointer-events:none;

z-index:-1;

}

.toastMessage{

position:fixed;

bottom:25px;

left:25px;

background:#0077ff;

color:white;

padding:16px 24px;

border-radius:10px;

display:none;

z-index:9999;

animation:fadeIn .4s;

}

.darkMode{

background:#111!important;

color:white!important;

}

.darkMode section{

background:#111!important;

color:white!important;

}

.darkMode .settingCard,

.darkMode .dashboardBox,

.darkMode .emergencyCard,

.darkMode .medicine,

.darkMode .statusCard{

background:#222!important;

color:white!important;

}

@keyframes fadeIn{

from{

opacity:0;

transform:translateY(20px);

}

to{

opacity:1;

transform:translateY(0);

}

}

</style>

<script>

function toggleDarkMode(){

document.body.classList.toggle("darkMode");

}

function changeThemeColor(){

let color=document.getElementById("themeColor").value;

document.documentElement.style.setProperty("--primary",color);

document.querySelectorAll("button").forEach(function(btn){

btn.style.background=color;

});

}

function showNotification(){

let toast=document.getElementById("toast");

toast.style.display="block";

setTimeout(function(){

toast.style.display="none";

},3000);

}

function changeLanguage(){

let lang=document.getElementById("languageSelect").value;

alert("Language changed to : "+lang);

}

const canvas=document.getElementById("particlesCanvas");

const ctx=canvas.getContext("2d");

canvas.width=window.innerWidth;

canvas.height=window.innerHeight;

let particles=[];

for(let i=0;i<80;i++){

particles.push({

x:Math.random()*canvas.width,

y:Math.random()*canvas.height,

r:Math.random()*3+1,

dx:(Math.random()-0.5),

dy:(Math.random()-0.5)

});

}

function animateParticles(){

ctx.clearRect(0,0,canvas.width,canvas.height);

particles.forEach(function(p){

ctx.beginPath();

ctx.arc(p.x,p.y,p.r,0,Math.PI*2);

ctx.fillStyle="#4aa3ff";

ctx.fill();

p.x+=p.dx;

p.y+=p.dy;

if(p.x<0)p.x=canvas.width;

if(p.x>canvas.width)p.x=0;

if(p.y<0)p.y=canvas.height;

if(p.y>canvas.height)p.y=0;

});

requestAnimationFrame(animateParticles);

}

animateParticles();

window.onresize=function(){

canvas.width=window.innerWidth;

canvas.height=window.innerHeight;

};

</script>
<!-- ================= PART 4D ================= -->

<section class="healthAnalytics">

<h2 class="title">❤️ Health Analytics</h2>

<div class="analyticsGrid">

<div class="analyticsCard">
<h3>Heart Rate</h3>
<h1 id="heartRate">72 BPM</h1>
</div>

<div class="analyticsCard">
<h3>Blood Pressure</h3>
<h1>120 / 80</h1>
</div>

<div class="analyticsCard">
<h3>Oxygen</h3>
<h1>98%</h1>
</div>

<div class="analyticsCard">
<h3>Temperature</h3>
<h1>36.8°C</h1>
</div>

</div>

<div class="heartAnimation">

<div class="heart"></div>

</div>

</section>

<section class="calendarSection">

<h2 class="title">📅 Appointment Calendar</h2>

<div class="calendarBox">

<input type="date" id="appointmentDate">

<button onclick="saveAppointmentDate()">

Save Appointment

</button>

<p id="calendarResult"></p>

</div>

</section>

<section class="hospitalMap">

<h2 class="title">🗺 Hospital Navigation</h2>

<div class="mapBox">

🏥 Interactive Hospital Map

</div>

</section>

<div id="welcomePopup" class="popup">

<h2>🎉 Welcome</h2>

<p>Thank you for choosing CarePlus Hospital.</p>

<button onclick="closePopup()">

Close

</button>

</div>

<style>

.healthAnalytics{

padding:90px 8%;

background:#f8fbff;

}

.analyticsGrid{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:25px;

}

.analyticsCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 12px 30px rgba(0,0,0,.08);

}

.analyticsCard h1{

font-size:42px;

color:#0077ff;

}

.heartAnimation{

display:flex;

justify-content:center;

padding:60px;

}

.heart{

width:120px;

height:120px;

background:red;

transform:rotate(-45deg);

animation:beat 1s infinite;

position:relative;

}

.heart:before,

.heart:after{

content:"";

width:120px;

height:120px;

background:red;

border-radius:50%;

position:absolute;

}

.heart:before{

top:-60px;

left:0;

}

.heart:after{

left:60px;

top:0;

}

@keyframes beat{

0%{transform:rotate(-45deg) scale(1);}

50%{transform:rotate(-45deg) scale(1.2);}

100%{transform:rotate(-45deg) scale(1);}

}

.calendarSection{

padding:90px 8%;

text-align:center;

}

.calendarBox{

max-width:500px;

margin:auto;

background:white;

padding:35px;

border-radius:20px;

box-shadow:0 12px 30px rgba(0,0,0,.08);

}

.calendarBox input{

width:100%;

padding:16px;

margin:20px 0;

border-radius:10px;

border:1px solid #ccc;

}

.calendarBox button{

padding:15px 30px;

background:#0077ff;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

}

.hospitalMap{

padding:90px 8%;

background:#eef7ff;

}

.mapBox{

height:420px;

display:flex;

align-items:center;

justify-content:center;

background:#ddd;

font-size:34px;

border-radius:20px;

}

.popup{

position:fixed;

top:50%;

left:50%;

transform:translate(-50%,-50%);

background:white;

padding:40px;

border-radius:20px;

box-shadow:0 15px 40px rgba(0,0,0,.2);

display:none;

z-index:9999;

text-align:center;

}

.popup button{

margin-top:20px;

padding:12px 25px;

background:#0077ff;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

}

</style>

<script>

setInterval(function(){

let bpm=Math.floor(Math.random()*20)+65;

document.getElementById("heartRate").innerHTML=bpm+" BPM";

},3000);

function saveAppointmentDate(){

let date=document.getElementById("appointmentDate").value;

document.getElementById("calendarResult").innerHTML=

"✅ Appointment saved for "+date;

}

setTimeout(function(){

document.getElementById("welcomePopup").style.display="block";

},2000);

function closePopup(){

document.getElementById("welcomePopup").style.display="none";

}

</script>
<!-- ================= PART 5A ================= -->

<section class="paymentSection">

<h2 class="title">💳 Online Payment</h2>

<div class="paymentBox">

<input type="text" id="payName" placeholder="Patient Name">

<input type="number" id="payAmount" placeholder="Amount">

<select id="paymentMethod">

<option>UPI</option>
<option>Credit Card</option>
<option>Debit Card</option>
<option>Net Banking</option>

</select>

<button onclick="makePayment()">

Pay Now

</button>

<p id="paymentStatus"></p>

</div>

</section>

<section class="reportSection">

<h2 class="title">

📄 Upload Medical Reports

</h2>

<div class="uploadBox">

<input type="file" id="reportFile">

<button onclick="uploadReport()">

Upload Report

</button>

<p id="uploadStatus"></p>

</div>

</section>

<section class="labSection">

<h2 class="title">

🧪 Book Lab Test

</h2>

<div class="labBox">

<input type="text"

id="labPatient"

placeholder="Patient Name">

<select id="labTest">

<option>Blood Test</option>
<option>Sugar Test</option>
<option>ECG</option>
<option>X-Ray</option>
<option>MRI Scan</option>
<option>CT Scan</option>

</select>

<button onclick="bookLabTest()">

Book Test

</button>

<p id="labStatus"></p>

</div>

</section>

<section class="prescriptionSection">

<h2 class="title">

💊 Prescription

</h2>

<div class="prescriptionCard">

<h3>Current Medicines</h3>

<ul>

<li>Paracetamol - 2 Times Daily</li>

<li>Vitamin D - Morning</li>

<li>Calcium Tablet - Night</li>

<li>Blood Pressure Tablet - Daily</li>

</ul>

</div>

</section>

<style>

.paymentSection,
.reportSection,
.labSection,
.prescriptionSection{

padding:90px 8%;

background:#f8fbff;

}

.paymentBox,
.uploadBox,
.labBox,
.prescriptionCard{

max-width:600px;

margin:auto;

background:white;

padding:35px;

border-radius:20px;

box-shadow:0 15px 35px rgba(0,0,0,.08);

}

.paymentBox input,
.paymentBox select,
.labBox input,
.labBox select{

width:100%;

padding:15px;

margin:12px 0;

border-radius:10px;

border:1px solid #ccc;

}

button{

padding:15px 30px;

background:#0077ff;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

}

.prescriptionCard ul{

padding-left:25px;

}

.prescriptionCard li{

margin:12px 0;

}

</style>

<script>

function makePayment(){

let name=document.getElementById("payName").value;

let amount=document.getElementById("payAmount").value;

document.getElementById("paymentStatus").innerHTML=

"✅ ₹"+amount+" payment received from "+name;

}

function uploadReport(){

let file=document.getElementById("reportFile").files[0];

if(file){

document.getElementById("uploadStatus").innerHTML=

"✅ "+file.name+" uploaded successfully.";

}

}

function bookLabTest(){

let patient=document.getElementById("labPatient").value;

let test=document.getElementById("labTest").value;

document.getElementById("labStatus").innerHTML=

"🧪 "+test+" booked for "+patient;

}

</script>
<!-- ================= PART 5 - DOCTOR MANAGEMENT ================= -->

<section class="doctorManagement">

<h2 class="title">👨‍⚕️ Doctor Management</h2>

<div class="doctorForm">

<input type="text" id="doctorName" placeholder="Doctor Name">

<input type="text" id="doctorSpecialization" placeholder="Specialization">

<input type="text" id="doctorExperience" placeholder="Experience">

<button onclick="addDoctor()">

Add Doctor

</button>

</div>

<table class="doctorTable">

<thead>

<tr>

<th>ID</th>

<th>Name</th>

<th>Specialization</th>

<th>Experience</th>

</tr>

</thead>

<tbody id="doctorTableBody">

<tr>

<td>1</td>

<td>Dr. James Wilson</td>

<td>Cardiology</td>

<td>10 Years</td>

</tr>

<tr>

<td>2</td>

<td>Dr. Sarah Lee</td>

<td>Neurology</td>

<td>8 Years</td>

</tr>

</tbody>

</table>

</section>

<style>

.doctorManagement{

padding:90px 8%;

background:#f5fbff;

}

.doctorForm{

max-width:700px;

margin:auto;

display:grid;

gap:15px;

}

.doctorForm input{

padding:15px;

border-radius:10px;

border:1px solid #ccc;

}

.doctorForm button{

padding:15px;

background:#0077ff;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

}

.doctorTable{

width:100%;

margin-top:40px;

border-collapse:collapse;

background:white;

box-shadow:0 12px 25px rgba(0,0,0,.08);

}

.doctorTable th{

background:#0077ff;

color:white;

padding:15px;

}

.doctorTable td{

padding:15px;

border-bottom:1px solid #ddd;

text-align:center;

}

.doctorTable tr:hover{

background:#eef7ff;

}

</style>

<script>

let doctorCount=2;

function addDoctor(){

let name=document.getElementById("doctorName").value;

let spec=document.getElementById("doctorSpecialization").value;

let exp=document.getElementById("doctorExperience").value;

if(name==""||spec==""||exp==""){

alert("Fill all fields");

return;

}

doctorCount++;

let row=

"<tr>"+

"<td>"+doctorCount+"</td>"+

"<td>"+name+"</td>"+

"<td>"+spec+"</td>"+

"<td>"+exp+"</td>"+

"</tr>";

document.getElementById("doctorTableBody").innerHTML+=row;

document.getElementById("doctorName").value="";

document.getElementById("doctorSpecialization").value="";

document.getElementById("doctorExperience").value="";

alert("Doctor Added Successfully");

}

</script>
<!-- ================= PART 5 - PATIENT MANAGEMENT ================= -->

<section class="patientManagement">

<h2 class="title">🏥 Patient Management</h2>

<div class="patientForm">

<input type="text" id="patientName" placeholder="Patient Name">

<input type="number" id="patientAge" placeholder="Age">

<select id="patientGender">

<option>Male</option>

<option>Female</option>

<option>Other</option>

</select>

<input type="text" id="patientDisease" placeholder="Disease">

<input type="text" id="patientDoctor" placeholder="Doctor Assigned">

<button onclick="addPatient()">

Add Patient

</button>

</div>

<table class="patientTable">

<thead>

<tr>

<th>ID</th>

<th>Name</th>

<th>Age</th>

<th>Gender</th>

<th>Disease</th>

<th>Doctor</th>

<th>Status</th>

</tr>

</thead>

<tbody id="patientBody">

<tr>

<td>1</td>

<td>Mohamed</td>

<td>20</td>

<td>Male</td>

<td>Fever</td>

<td>Dr. James</td>

<td><span class="activeStatus">Admitted</span></td>

</tr>

</tbody>

</table>

</section>

<style>

.patientManagement{

padding:90px 8%;

background:#eef7ff;

}

.patientForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:35px;

}

.patientForm input,

.patientForm select{

padding:14px;

border-radius:10px;

border:1px solid #ccc;

}

.patientForm button{

padding:14px;

background:#0077ff;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

}

.patientTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 12px 25px rgba(0,0,0,.08);

}

.patientTable th{

background:#0077ff;

color:white;

padding:15px;

}

.patientTable td{

padding:14px;

text-align:center;

border-bottom:1px solid #eee;

}

.patientTable tr:hover{

background:#f3f8ff;

}

.activeStatus{

background:#28a745;

color:white;

padding:6px 12px;

border-radius:20px;

font-size:13px;

}

</style>

<script>

let patientID=1;

function addPatient(){

let name=document.getElementById("patientName").value;

let age=document.getElementById("patientAge").value;

let gender=document.getElementById("patientGender").value;

let disease=document.getElementById("patientDisease").value;

let doctor=document.getElementById("patientDoctor").value;

if(name==""||age==""||disease==""||doctor==""){

alert("Please fill all fields");

return;

}

patientID++;

let row="<tr>"+

"<td>"+patientID+"</td>"+

"<td>"+name+"</td>"+

"<td>"+age+"</td>"+

"<td>"+gender+"</td>"+

"<td>"+disease+"</td>"+

"<td>"+doctor+"</td>"+

"<td><span class='activeStatus'>Admitted</span></td>"+

"</tr>";

document.getElementById("patientBody").innerHTML+=row;

document.getElementById("patientName").value="";

document.getElementById("patientAge").value="";

document.getElementById("patientDisease").value="";

document.getElementById("patientDoctor").value="";

}

</script>
<!-- ================= PART 5 - PHARMACY INVENTORY ================= -->

<section class="pharmacyInventory">

<h2 class="title">💊 Pharmacy Inventory Management</h2>

<div class="inventoryForm">

<input type="text" id="medicineName" placeholder="Medicine Name">

<input type="text" id="medicineCompany" placeholder="Manufacturer">

<input type="number" id="medicinePrice" placeholder="Price (₹)">

<input type="number" id="medicineStock" placeholder="Stock Quantity">

<input type="date" id="medicineExpiry">

<button onclick="addMedicine()">

Add Medicine

</button>

</div>

<div class="searchBox">

<input type="text"

id="medicineSearch"

placeholder="🔍 Search Medicine..."

onkeyup="searchMedicine()">

</div>

<table class="inventoryTable">

<thead>

<tr>

<th>ID</th>

<th>Medicine</th>

<th>Company</th>

<th>Price</th>

<th>Stock</th>

<th>Expiry</th>

<th>Status</th>

</tr>

</thead>

<tbody id="inventoryBody">

<tr>

<td>1</td>

<td>Paracetamol 650</td>

<td>Cipla</td>

<td>₹35</td>

<td>250</td>

<td>2028-05-10</td>

<td><span class="available">Available</span></td>

</tr>

<tr>

<td>2</td>

<td>Amoxicillin</td>

<td>Sun Pharma</td>

<td>₹120</td>

<td>45</td>

<td>2027-12-15</td>

<td><span class="lowStock">Low Stock</span></td>

</tr>

</tbody>

</table>

</section>

<style>

.pharmacyInventory{

padding:90px 8%;

background:#f7fbff;

}

.inventoryForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:25px;

}

.inventoryForm input{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.inventoryForm button{

padding:15px;

background:#0077ff;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.searchBox{

margin-bottom:20px;

}

.searchBox input{

width:100%;

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.inventoryTable{

width:100%;

border-collapse:collapse;

background:white;

box-shadow:0 12px 25px rgba(0,0,0,.08);

border-radius:15px;

overflow:hidden;

}

.inventoryTable th{

background:#0077ff;

color:white;

padding:15px;

}

.inventoryTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.inventoryTable tr:hover{

background:#eef7ff;

}

.available{

background:#28a745;

color:white;

padding:6px 12px;

border-radius:20px;

font-size:13px;

}

.lowStock{

background:#ff9800;

color:white;

padding:6px 12px;

border-radius:20px;

font-size:13px;

}

.outStock{

background:#e53935;

color:white;

padding:6px 12px;

border-radius:20px;

font-size:13px;

}

</style>

<script>

let medicineID=2;

function addMedicine(){

let name=document.getElementById("medicineName").value;

let company=document.getElementById("medicineCompany").value;

let price=document.getElementById("medicinePrice").value;

let stock=document.getElementById("medicineStock").value;

let expiry=document.getElementById("medicineExpiry").value;

if(name==""||company==""||price==""||stock==""||expiry==""){

alert("Please fill all fields");

return;

}

medicineID++;

let status="<span class='available'>Available</span>";

if(stock<50){

status="<span class='lowStock'>Low Stock</span>";

}

if(stock==0){

status="<span class='outStock'>Out of Stock</span>";

}

let row="<tr>"+

"<td>"+medicineID+"</td>"+

"<td>"+name+"</td>"+

"<td>"+company+"</td>"+

"<td>₹"+price+"</td>"+

"<td>"+stock+"</td>"+

"<td>"+expiry+"</td>"+

"<td>"+status+"</td>"+

"</tr>";

document.getElementById("inventoryBody").innerHTML+=row;

document.getElementById("medicineName").value="";

document.getElementById("medicineCompany").value="";

document.getElementById("medicinePrice").value="";

document.getElementById("medicineStock").value="";

document.getElementById("medicineExpiry").value="";

alert("Medicine Added Successfully");

}

function searchMedicine(){

let input=document.getElementById("medicineSearch").value.toUpperCase();

let table=document.getElementById("inventoryBody");

let rows=table.getElementsByTagName("tr");

for(let i=0;i<rows.length;i++){

let cell=rows[i].getElementsByTagName("td")[1];

if(cell){

let txt=cell.textContent||cell.innerText;

rows[i].style.display=txt.toUpperCase().indexOf(input)>-1?"":"none";

}

}

}

</script>
<!-- ================= BILLING MANAGEMENT ================= -->

<section class="billingSection">

<h2 class="title">💰 Hospital Billing</h2>

<div class="billingForm">

<input type="text" id="billPatient" placeholder="Patient Name">

<input type="text" id="billTreatment" placeholder="Treatment">

<input type="number" id="doctorFee" placeholder="Doctor Fee">

<input type="number" id="medicineFee" placeholder="Medicine Fee">

<input type="number" id="labFee" placeholder="Lab Fee">

<button onclick="generateBill()">

Generate Bill

</button>

</div>

<div class="invoiceCard">

<h2>Invoice</h2>

<hr>

<p><b>Patient :</b> <span id="invoicePatient">-</span></p>

<p><b>Treatment :</b> <span id="invoiceTreatment">-</span></p>

<p><b>Doctor Fee :</b> ₹<span id="invoiceDoctor">0</span></p>

<p><b>Medicine :</b> ₹<span id="invoiceMedicine">0</span></p>

<p><b>Lab Charge :</b> ₹<span id="invoiceLab">0</span></p>

<hr>

<h2>

Total : ₹<span id="invoiceTotal">0</span>

</h2>

<button onclick="window.print()">

🖨 Print Invoice

</button>

</div>

</section>

<style>

.billingSection{

padding:90px 8%;

background:#eef8ff;

display:grid;

grid-template-columns:1fr 1fr;

gap:40px;

}

.billingForm{

background:white;

padding:30px;

border-radius:20px;

box-shadow:0 10px 25px rgba(0,0,0,.08);

}

.billingForm input{

width:100%;

padding:15px;

margin:10px 0;

border-radius:10px;

border:1px solid #ccc;

}

.billingForm button{

width:100%;

padding:15px;

background:#0077ff;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-size:18px;

}

.invoiceCard{

background:white;

padding:35px;

border-radius:20px;

box-shadow:0 10px 25px rgba(0,0,0,.08);

}

.invoiceCard p{

font-size:18px;

margin:15px 0;

}

.invoiceCard h2{

color:#0077ff;

}

.invoiceCard button{

margin-top:20px;

padding:15px 25px;

background:#28a745;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

}

@media(max-width:900px){

.billingSection{

grid-template-columns:1fr;

}

}

</style>

<script>

function generateBill(){

let patient=document.getElementById("billPatient").value;

let treatment=document.getElementById("billTreatment").value;

let doctor=parseFloat(document.getElementById("doctorFee").value)||0;

let medicine=parseFloat(document.getElementById("medicineFee").value)||0;

let lab=parseFloat(document.getElementById("labFee").value)||0;

let total=doctor+medicine+lab;

document.getElementById("invoicePatient").innerHTML=patient;

document.getElementById("invoiceTreatment").innerHTML=treatment;

document.getElementById("invoiceDoctor").innerHTML=doctor;

document.getElementById("invoiceMedicine").innerHTML=medicine;

document.getElementById("invoiceLab").innerHTML=lab;

document.getElementById("invoiceTotal").innerHTML=total;

}

</script>
<!-- ================= STAFF MANAGEMENT ================= -->

<section class="staffSection">

<h2 class="title">👨‍💼 Hospital Staff Management</h2>

<div class="staffForm">

<input type="text" id="staffName" placeholder="Staff Name">

<input type="text" id="staffRole" placeholder="Role">

<input type="text" id="staffDepartment" placeholder="Department">

<input type="text" id="staffPhone" placeholder="Phone Number">

<button onclick="addStaff()">

Add Staff

</button>

</div>

<table class="staffTable">

<thead>

<tr>

<th>ID</th>

<th>Name</th>

<th>Role</th>

<th>Department</th>

<th>Phone</th>

<th>Status</th>

</tr>

</thead>

<tbody id="staffBody">

<tr>

<td>1</td>

<td>Rahul Kumar</td>

<td>Nurse</td>

<td>Emergency</td>

<td>9876543210</td>

<td><span class="online">Available</span></td>

</tr>

<tr>

<td>2</td>

<td>Anita Sharma</td>

<td>Receptionist</td>

<td>Front Desk</td>

<td>9123456789</td>

<td><span class="offline">Off Duty</span></td>

</tr>

</tbody>

</table>

</section>

<style>

.staffSection{

padding:90px 8%;

background:#f7fbff;

}

.staffForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.staffForm input{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.staffForm button{

padding:15px;

background:#0077ff;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-size:16px;

}

.staffTable{

width:100%;

border-collapse:collapse;

background:white;

box-shadow:0 10px 25px rgba(0,0,0,.08);

border-radius:15px;

overflow:hidden;

}

.staffTable th{

background:#0077ff;

color:white;

padding:15px;

}

.staffTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.staffTable tr:hover{

background:#eef6ff;

}

.online{

background:#28a745;

color:white;

padding:6px 12px;

border-radius:20px;

}

.offline{

background:#dc3545;

color:white;

padding:6px 12px;

border-radius:20px;

}

</style>

<script>

let staffID=2;

function addStaff(){

let name=document.getElementById("staffName").value;

let role=document.getElementById("staffRole").value;

let dept=document.getElementById("staffDepartment").value;

let phone=document.getElementById("staffPhone").value;

if(name==""||role==""||dept==""||phone==""){

alert("Please fill all fields");

return;

}

staffID++;

let row="<tr>"+

"<td>"+staffID+"</td>"+

"<td>"+name+"</td>"+

"<td>"+role+"</td>"+

"<td>"+dept+"</td>"+

"<td>"+phone+"</td>"+

"<td><span class='online'>Available</span></td>"+

"</tr>";

document.getElementById("staffBody").innerHTML+=row;

document.getElementById("staffName").value="";

document.getElementById("staffRole").value="";

document.getElementById("staffDepartment").value="";

document.getElementById("staffPhone").value="";

alert("Staff Added Successfully");

}

</script><!-- ================= AMBULANCE MANAGEMENT ================= -->

<section class="ambulanceSection">

<h2 class="title">🚑 Ambulance Management</h2>

<div class="ambulanceForm">

<input type="text" id="driverName" placeholder="Driver Name">

<input type="text" id="vehicleNumber" placeholder="Vehicle Number">

<input type="text" id="patientLocation" placeholder="Pickup Location">

<select id="ambulanceStatus">

<option>Available</option>

<option>On Duty</option>

<option>Maintenance</option>

</select>

<button onclick="addAmbulance()">

Add Ambulance

</button>

</div>

<table class="ambulanceTable">

<thead>

<tr>

<th>ID</th>

<th>Driver</th>

<th>Vehicle No</th>

<th>Location</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="ambulanceBody">

<tr>

<td>1</td>

<td>Ravi Kumar</td>

<td>TN37AB1234</td>

<td>Coimbatore</td>

<td><span class="available">Available</span></td>

<td><button onclick="dispatch(this)">Dispatch</button></td>

</tr>

</tbody>

</table>

</section>

<style>

.ambulanceSection{

padding:90px 8%;

background:#eef8ff;

}

.ambulanceForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.ambulanceForm input,

.ambulanceForm select{

padding:15px;

border-radius:10px;

border:1px solid #ccc;

}

.ambulanceForm button{

padding:15px;

background:#e53935;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.ambulanceTable{

width:100%;

border-collapse:collapse;

background:white;

box-shadow:0 12px 25px rgba(0,0,0,.08);

border-radius:15px;

overflow:hidden;

}

.ambulanceTable th{

background:#e53935;

color:white;

padding:15px;

}

.ambulanceTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.ambulanceTable tr:hover{

background:#fff3f3;

}

.available{

background:#28a745;

color:white;

padding:6px 12px;

border-radius:20px;

}

.onduty{

background:#ff9800;

color:white;

padding:6px 12px;

border-radius:20px;

}

.maintenance{

background:#607d8b;

color:white;

padding:6px 12px;

border-radius:20px;

}

.ambulanceTable button{

padding:8px 16px;

background:#0077ff;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let ambulanceID=1;

function addAmbulance(){

let driver=document.getElementById("driverName").value;

let vehicle=document.getElementById("vehicleNumber").value;

let location=document.getElementById("patientLocation").value;

let status=document.getElementById("ambulanceStatus").value;

if(driver==""||vehicle==""||location==""){

alert("Fill all fields");

return;

}

ambulanceID++;

let badge="<span class='available'>Available</span>";

if(status=="On Duty")

badge="<span class='onduty'>On Duty</span>";

if(status=="Maintenance")

badge="<span class='maintenance'>Maintenance</span>";

let row="<tr>"+

"<td>"+ambulanceID+"</td>"+

"<td>"+driver+"</td>"+

"<td>"+vehicle+"</td>"+

"<td>"+location+"</td>"+

"<td>"+badge+"</td>"+

"<td><button onclick='dispatch(this)'>Dispatch</button></td>"+

"</tr>";

document.getElementById("ambulanceBody").innerHTML+=row;

document.getElementById("driverName").value="";

document.getElementById("vehicleNumber").value="";

document.getElementById("patientLocation").value="";

}

function dispatch(btn){

let row=btn.parentElement.parentElement;

row.cells[4].innerHTML="<span class='onduty'>On Duty</span>";

alert("🚑 Ambulance dispatched successfully.");

}

</script>
<!-- ================= LABORATORY MANAGEMENT ================= -->

<section class="labManagement">

<h2 class="title">🧪 Laboratory Management</h2>

<div class="labForm">

<input type="text" id="testPatient" placeholder="Patient Name">

<select id="testType">

<option>Blood Test</option>

<option>Urine Test</option>

<option>ECG</option>

<option>X-Ray</option>

<option>MRI Scan</option>

<option>CT Scan</option>

<option>COVID Test</option>

</select>

<input type="text" id="labDoctor" placeholder="Doctor Name">

<input type="date" id="labDate">

<button onclick="addLabTest()">

Book Test

</button>

</div>

<table class="labTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Test</th>

<th>Doctor</th>

<th>Date</th>

<th>Status</th>

<th>Report</th>

</tr>

</thead>

<tbody id="labBody">

<tr>

<td>1</td>

<td>Mohamed</td>

<td>Blood Test</td>

<td>Dr. James</td>

<td>2026-07-29</td>

<td><span class="pending">Pending</span></td>

<td><button onclick="completeReport(this)">Complete</button></td>

</tr>

</tbody>

</table>

</section>

<style>

.labManagement{

padding:90px 8%;

background:#f8fbff;

}

.labForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.labForm input,

.labForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.labForm button{

padding:15px;

background:#673ab7;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.labTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 12px 25px rgba(0,0,0,.08);

}

.labTable th{

background:#673ab7;

color:white;

padding:15px;

}

.labTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.labTable tr:hover{

background:#f4eeff;

}

.pending{

background:#ff9800;

color:white;

padding:6px 12px;

border-radius:20px;

}

.completed{

background:#28a745;

color:white;

padding:6px 12px;

border-radius:20px;

}

.labTable button{

padding:8px 16px;

background:#0077ff;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let labID=1;

function addLabTest(){

let patient=document.getElementById("testPatient").value;

let test=document.getElementById("testType").value;

let doctor=document.getElementById("labDoctor").value;

let date=document.getElementById("labDate").value;

if(patient==""||doctor==""||date==""){

alert("Please fill all fields");

return;

}

labID++;

let row="<tr>"+

"<td>"+labID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+test+"</td>"+

"<td>"+doctor+"</td>"+

"<td>"+date+"</td>"+

"<td><span class='pending'>Pending</span></td>"+

"<td><button onclick='completeReport(this)'>Complete</button></td>"+

"</tr>";

document.getElementById("labBody").innerHTML+=row;

document.getElementById("testPatient").value="";

document.getElementById("labDoctor").value="";

document.getElementById("labDate").value="";

}

function completeReport(btn){

let row=btn.parentElement.parentElement;

row.cells[5].innerHTML="<span class='completed'>Completed</span>";

btn.innerHTML="Download";

btn.onclick=function(){

alert("📄 Laboratory Report Downloaded");

};

}

</script>
<!-- ================= BLOOD BANK MANAGEMENT ================= -->

<section class="bloodBankSection">

<h2 class="title">🩸 Blood Bank Management</h2>

<div class="bloodForm">

<input type="text" id="donorName" placeholder="Donor Name">

<select id="bloodGroup">

<option>A+</option>
<option>A-</option>
<option>B+</option>
<option>B-</option>
<option>AB+</option>
<option>AB-</option>
<option>O+</option>
<option>O-</option>

</select>

<input type="number" id="bloodUnits" placeholder="Units">

<input type="date" id="donationDate">

<button onclick="addBlood()">

Add Blood

</button>

</div>

<table class="bloodTable">

<thead>

<tr>

<th>ID</th>

<th>Donor</th>

<th>Blood Group</th>

<th>Units</th>

<th>Date</th>

<th>Status</th>

</tr>

</thead>

<tbody id="bloodBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>O+</td>

<td>2</td>

<td>2026-07-29</td>

<td><span class="available">Available</span></td>

</tr>

</tbody>

</table>

</section>

<style>

.bloodBankSection{

padding:90px 8%;

background:#fff7f7;

}

.bloodForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.bloodForm input,
.bloodForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.bloodForm button{

padding:15px;

background:#d32f2f;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.bloodTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 12px 25px rgba(0,0,0,.08);

}

.bloodTable th{

background:#d32f2f;

color:white;

padding:15px;

}

.bloodTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.available{

background:#28a745;

color:white;

padding:6px 12px;

border-radius:20px;

}

.low{

background:#ff9800;

color:white;

padding:6px 12px;

border-radius:20px;

}

</style>

<script>

let bloodID=1;

function addBlood(){

let donor=document.getElementById("donorName").value;

let group=document.getElementById("bloodGroup").value;

let units=parseInt(document.getElementById("bloodUnits").value);

let date=document.getElementById("donationDate").value;

if(donor==""||!units||date==""){

alert("Please fill all fields");

return;

}

bloodID++;

let status="<span class='available'>Available</span>";

if(units<=2){

status="<span class='low'>Low Stock</span>";

}

let row="<tr>"+

"<td>"+bloodID+"</td>"+

"<td>"+donor+"</td>"+

"<td>"+group+"</td>"+

"<td>"+units+"</td>"+

"<td>"+date+"</td>"+

"<td>"+status+"</td>"+

"</tr>";

document.getElementById("bloodBody").innerHTML+=row;

document.getElementById("donorName").value="";

document.getElementById("bloodUnits").value="";

document.getElementById("donationDate").value="";

}

</script>
<!-- ================= BED MANAGEMENT ================= -->

<section class="bedSection">

<h2 class="title">🛏️ Bed Management</h2>

<div class="bedForm">

<input type="text" id="bedPatient" placeholder="Patient Name">

<select id="bedWard">

<option>General Ward</option>
<option>ICU</option>
<option>Emergency</option>
<option>Maternity</option>
<option>Pediatric</option>
<option>VIP Room</option>

</select>

<input type="number" id="bedNumber" placeholder="Bed Number">

<button onclick="assignBed()">

Assign Bed

</button>

</div>

<div class="bedStats">

<div class="bedCard">

<h1 id="totalBeds">250</h1>

<p>Total Beds</p>

</div>

<div class="bedCard">

<h1 id="availableBeds">180</h1>

<p>Available</p>

</div>

<div class="bedCard">

<h1 id="occupiedBeds">70</h1>

<p>Occupied</p>

</div>

</div>

<table class="bedTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Ward</th>

<th>Bed No</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="bedBody">

<tr>

<td>1</td>

<td>Mohamed Haris</td>

<td>General Ward</td>

<td>101</td>

<td><span class="occupied">Occupied</span></td>

<td>

<button onclick="dischargePatient(this)">

Discharge

</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.bedSection{

padding:90px 8%;

background:#eef9ff;

}

.bedForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.bedForm input,

.bedForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.bedForm button{

padding:15px;

background:#2196f3;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.bedStats{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(200px,1fr));

gap:20px;

margin-bottom:35px;

}

.bedCard{

background:white;

padding:30px;

border-radius:20px;

text-align:center;

box-shadow:0 10px 25px rgba(0,0,0,.08);

}

.bedCard h1{

font-size:48px;

color:#2196f3;

}

.bedTable{

width:100%;

background:white;

border-collapse:collapse;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 25px rgba(0,0,0,.08);

}

.bedTable th{

background:#2196f3;

color:white;

padding:15px;

}

.bedTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.bedTable tr:hover{

background:#f4fbff;

}

.available{

background:#28a745;

color:white;

padding:6px 14px;

border-radius:20px;

}

.occupied{

background:#ff5722;

color:white;

padding:6px 14px;

border-radius:20px;

}

.bedTable button{

padding:8px 18px;

background:#e53935;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let bedID=1;

let available=180;

let occupied=70;

function assignBed(){

let patient=document.getElementById("bedPatient").value;

let ward=document.getElementById("bedWard").value;

let bed=document.getElementById("bedNumber").value;

if(patient==""||bed==""){

alert("Please fill all fields");

return;

}

bedID++;

available--;

occupied++;

document.getElementById("availableBeds").innerHTML=available;

document.getElementById("occupiedBeds").innerHTML=occupied;

let row="<tr>"+

"<td>"+bedID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+ward+"</td>"+

"<td>"+bed+"</td>"+

"<td><span class='occupied'>Occupied</span></td>"+

"<td><button onclick='dischargePatient(this)'>Discharge</button></td>"+

"</tr>";

document.getElementById("bedBody").innerHTML+=row;

document.getElementById("bedPatient").value="";

document.getElementById("bedNumber").value="";

}

function dischargePatient(btn){

btn.parentElement.parentElement.remove();

available++;

occupied--;

document.getElementById("availableBeds").innerHTML=available;

document.getElementById("occupiedBeds").innerHTML=occupied;

alert("✅ Patient discharged successfully.");

}

</script>
<!-- ================= ICU MANAGEMENT ================= -->

<section class="icuSection">

<h2 class="title">🏥 ICU Management</h2>

<div class="icuForm">

<input type="text" id="icuPatient" placeholder="Patient Name">

<input type="number" id="icuAge" placeholder="Age">

<select id="icuCondition">

<option>Critical</option>
<option>Serious</option>
<option>Stable</option>

</select>

<select id="icuVentilator">

<option>Ventilator Required</option>
<option>No Ventilator</option>

</select>

<button onclick="addICUPatient()">

Admit to ICU

</button>

</div>

<div class="icuStats">

<div class="icuCard">

<h1 id="icuTotal">40</h1>

<p>Total ICU Beds</p>

</div>

<div class="icuCard">

<h1 id="icuAvailable">15</h1>

<p>Available Beds</p>

</div>

<div class="icuCard">

<h1 id="icuOccupied">25</h1>

<p>Occupied Beds</p>

</div>

</div>

<table class="icuTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Age</th>

<th>Condition</th>

<th>Ventilator</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="icuBody">

<tr>

<td>1</td>

<td>Rajesh Kumar</td>

<td>54</td>

<td>Critical</td>

<td>Yes</td>

<td><span class="criticalStatus">Critical</span></td>

<td>

<button onclick="dischargeICU(this)">

Discharge

</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.icuSection{

padding:90px 8%;

background:#f9fcff;

}

.icuForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.icuForm input,
.icuForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.icuForm button{

padding:15px;

background:#8e24aa;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.icuStats{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(200px,1fr));

gap:20px;

margin-bottom:30px;

}

.icuCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 25px rgba(0,0,0,.08);

}

.icuCard h1{

font-size:48px;

color:#8e24aa;

}

.icuTable{

width:100%;

background:white;

border-collapse:collapse;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 25px rgba(0,0,0,.08);

}

.icuTable th{

background:#8e24aa;

color:white;

padding:15px;

}

.icuTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.criticalStatus{

background:#e53935;

color:white;

padding:6px 12px;

border-radius:20px;

}

.seriousStatus{

background:#ff9800;

color:white;

padding:6px 12px;

border-radius:20px;

}

.stableStatus{

background:#28a745;

color:white;

padding:6px 12px;

border-radius:20px;

}

.icuTable button{

padding:8px 18px;

background:#d32f2f;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let icuID=1;

let icuAvailableBeds=15;

let icuOccupiedBeds=25;

function addICUPatient(){

let patient=document.getElementById("icuPatient").value;

let age=document.getElementById("icuAge").value;

let condition=document.getElementById("icuCondition").value;

let ventilator=document.getElementById("icuVentilator").value;

if(patient==""||age==""){

alert("Please fill all fields");

return;

}

icuID++;

icuAvailableBeds--;

icuOccupiedBeds++;

document.getElementById("icuAvailable").innerHTML=icuAvailableBeds;

document.getElementById("icuOccupied").innerHTML=icuOccupiedBeds;

let status="<span class='stableStatus'>Stable</span>";

if(condition=="Critical"){

status="<span class='criticalStatus'>Critical</span>";

}

if(condition=="Serious"){

status="<span class='seriousStatus'>Serious</span>";

}

let vent=(ventilator=="Ventilator Required")?"Yes":"No";

let row="<tr>"+

"<td>"+icuID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+age+"</td>"+

"<td>"+condition+"</td>"+

"<td>"+vent+"</td>"+

"<td>"+status+"</td>"+

"<td><button onclick='dischargeICU(this)'>Discharge</button></td>"+

"</tr>";

document.getElementById("icuBody").innerHTML+=row;

document.getElementById("icuPatient").value="";

document.getElementById("icuAge").value="";

}

function dischargeICU(btn){

btn.parentElement.parentElement.remove();

icuAvailableBeds++;

icuOccupiedBeds--;

document.getElementById("icuAvailable").innerHTML=icuAvailableBeds;

document.getElementById("icuOccupied").innerHTML=icuOccupiedBeds;

alert("✅ ICU Patient Discharged");

}

</script>
<!-- ================= VACCINATION MANAGEMENT ================= -->

<section class="vaccineSection">

<h2 class="title">💉 Vaccination Management</h2>

<div class="vaccineForm">

<input type="text" id="vacPatient" placeholder="Patient Name">

<input type="number" id="vacAge" placeholder="Age">

<select id="vacType">

<option>COVID-19</option>
<option>Hepatitis B</option>
<option>BCG</option>
<option>Polio</option>
<option>MMR</option>
<option>Tetanus</option>
<option>Influenza</option>

</select>

<input type="date" id="vacDate">

<input type="text" id="vacNurse" placeholder="Nurse Name">

<button onclick="addVaccination()">

Schedule Vaccine

</button>

</div>

<table class="vaccineTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Age</th>

<th>Vaccine</th>

<th>Date</th>

<th>Nurse</th>

<th>Status</th>

</tr>

</thead>

<tbody id="vaccineBody">

<tr>

<td>1</td>

<td>Mohamed</td>

<td>20</td>

<td>COVID-19</td>

<td>2026-08-10</td>

<td>Nurse Priya</td>

<td><span class="scheduled">Scheduled</span></td>

</tr>

</tbody>

</table>

</section>

<style>

.vaccineSection{

padding:90px 8%;

background:#f7fffb;

}

.vaccineForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.vaccineForm input,

.vaccineForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.vaccineForm button{

padding:15px;

background:#00a651;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.vaccineTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 12px 25px rgba(0,0,0,.08);

}

.vaccineTable th{

background:#00a651;

color:white;

padding:15px;

}

.vaccineTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.vaccineTable tr:hover{

background:#f0fff5;

}

.scheduled{

background:#ff9800;

color:white;

padding:6px 12px;

border-radius:20px;

}

.completed{

background:#28a745;

color:white;

padding:6px 12px;

border-radius:20px;

}

.vaccineTable button{

padding:8px 18px;

background:#0077ff;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let vaccineID=1;

function addVaccination(){

let patient=document.getElementById("vacPatient").value;

let age=document.getElementById("vacAge").value;

let vaccine=document.getElementById("vacType").value;

let date=document.getElementById("vacDate").value;

let nurse=document.getElementById("vacNurse").value;

if(patient==""||age==""||date==""||nurse==""){

alert("Please fill all fields");

return;

}

vaccineID++;

let row="<tr>"+

"<td>"+vaccineID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+age+"</td>"+

"<td>"+vaccine+"</td>"+

"<td>"+date+"</td>"+

"<td>"+nurse+"</td>"+

"<td><span class='scheduled'>Scheduled</span></td>"+

"</tr>";

document.getElementById("vaccineBody").innerHTML+=row;

document.getElementById("vacPatient").value="";

document.getElementById("vacAge").value="";

document.getElementById("vacDate").value="";

document.getElementById("vacNurse").value="";

alert("💉 Vaccination Scheduled Successfully");

}

</script>
<!-- ================= OPERATION THEATRE MANAGEMENT ================= -->

<section class="otSection">

<h2 class="title">🏥 Operation Theatre Management</h2>

<div class="otForm">

<input type="text" id="otPatient" placeholder="Patient Name">

<input type="text" id="otDoctor" placeholder="Surgeon Name">

<select id="otType">

<option>Heart Surgery</option>
<option>Brain Surgery</option>
<option>Orthopedic Surgery</option>
<option>General Surgery</option>
<option>ENT Surgery</option>
<option>Eye Surgery</option>

</select>

<input type="date" id="otDate">

<input type="time" id="otTime">

<button onclick="scheduleOT()">

Schedule Surgery

</button>

</div>

<div class="otCards">

<div class="otCard">

<h1 id="otRooms">8</h1>

<p>Total OT Rooms</p>

</div>

<div class="otCard">

<h1 id="otAvailable">5</h1>

<p>Available</p>

</div>

<div class="otCard">

<h1 id="otBusy">3</h1>

<p>Occupied</p>

</div>

</div>

<table class="otTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Doctor</th>

<th>Surgery</th>

<th>Date</th>

<th>Time</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="otBody">

<tr>

<td>1</td>

<td>Mohamed</td>

<td>Dr. James</td>

<td>Heart Surgery</td>

<td>2026-08-02</td>

<td>09:30 AM</td>

<td><span class="scheduled">Scheduled</span></td>

<td>

<button onclick="startOT(this)">

Start

</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.otSection{

padding:90px 8%;

background:#eef8ff;

}

.otForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.otForm input,

.otForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.otForm button{

padding:15px;

background:#1565c0;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.otCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.otCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 25px rgba(0,0,0,.08);

}

.otCard h1{

font-size:50px;

color:#1565c0;

}

.otTable{

width:100%;

border-collapse:collapse;

background:white;

box-shadow:0 10px 25px rgba(0,0,0,.08);

border-radius:15px;

overflow:hidden;

}

.otTable th{

background:#1565c0;

color:white;

padding:15px;

}

.otTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.scheduled{

background:#ff9800;

color:white;

padding:6px 12px;

border-radius:20px;

}

.running{

background:#2196f3;

color:white;

padding:6px 12px;

border-radius:20px;

}

.completed{

background:#4caf50;

color:white;

padding:6px 12px;

border-radius:20px;

}

.otTable button{

padding:8px 18px;

background:#1565c0;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let otID=1;

let availableOT=5;

let busyOT=3;

function scheduleOT(){

let patient=document.getElementById("otPatient").value;

let doctor=document.getElementById("otDoctor").value;

let surgery=document.getElementById("otType").value;

let date=document.getElementById("otDate").value;

let time=document.getElementById("otTime").value;

if(patient==""||doctor==""||date==""||time==""){

alert("Please fill all fields");

return;

}

otID++;

availableOT--;

busyOT++;

document.getElementById("otAvailable").innerHTML=availableOT;

document.getElementById("otBusy").innerHTML=busyOT;

let row="<tr>"+

"<td>"+otID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+doctor+"</td>"+

"<td>"+surgery+"</td>"+

"<td>"+date+"</td>"+

"<td>"+time+"</td>"+

"<td><span class='scheduled'>Scheduled</span></td>"+

"<td><button onclick='startOT(this)'>Start</button></td>"+

"</tr>";

document.getElementById("otBody").innerHTML+=row;

document.getElementById("otPatient").value="";

document.getElementById("otDoctor").value="";

document.getElementById("otDate").value="";

document.getElementById("otTime").value="";

}

function startOT(btn){

let row=btn.parentElement.parentElement;

row.cells[6].innerHTML="<span class='running'>Running</span>";

btn.innerHTML="Complete";

btn.onclick=function(){

row.cells[6].innerHTML="<span class='completed'>Completed</span>";

this.disabled=true;

this.innerHTML="Done";

availableOT++;

busyOT--;

document.getElementById("otAvailable").innerHTML=availableOT;

document.getElementById("otBusy").innerHTML=busyOT;

};

}

</script><!-- ================= INSURANCE MANAGEMENT ================= -->

<section class="insuranceSection">

<h2 class="title">🧾 Insurance Claim Management</h2>

<div class="insuranceForm">

<input type="text" id="insPatient" placeholder="Patient Name">

<input type="text" id="insCompany" placeholder="Insurance Company">

<input type="text" id="insPolicy" placeholder="Policy Number">

<input type="number" id="insAmount" placeholder="Claim Amount (₹)">

<select id="insStatus">

<option>Pending</option>

<option>Approved</option>

<option>Rejected</option>

</select>

<button onclick="addClaim()">

Submit Claim

</button>

</div>

<div class="insuranceStats">

<div class="insuranceCard">

<h1 id="totalClaims">15</h1>

<p>Total Claims</p>

</div>

<div class="insuranceCard">

<h1 id="approvedClaims">9</h1>

<p>Approved</p>

</div>

<div class="insuranceCard">

<h1 id="pendingClaims">6</h1>

<p>Pending</p>

</div>

</div>

<table class="insuranceTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Company</th>

<th>Policy</th>

<th>Amount</th>

<th>Status</th>

</tr>

</thead>

<tbody id="insuranceBody">

<tr>

<td>1</td>

<td>Mohamed</td>

<td>Star Health</td>

<td>SH458962</td>

<td>₹25000</td>

<td><span class="pendingStatus">Pending</span></td>

</tr>

</tbody>

</table>

</section>

<style>

.insuranceSection{

padding:90px 8%;

background:#f8fbff;

}

.insuranceForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.insuranceForm input,

.insuranceForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.insuranceForm button{

padding:15px;

background:#3949ab;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.insuranceStats{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.insuranceCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 25px rgba(0,0,0,.08);

}

.insuranceCard h1{

font-size:48px;

color:#3949ab;

}

.insuranceTable{

width:100%;

background:white;

border-collapse:collapse;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 25px rgba(0,0,0,.08);

}

.insuranceTable th{

background:#3949ab;

color:white;

padding:15px;

}

.insuranceTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.pendingStatus{

background:#ff9800;

color:white;

padding:6px 12px;

border-radius:20px;

}

.approvedStatus{

background:#4caf50;

color:white;

padding:6px 12px;

border-radius:20px;

}

.rejectedStatus{

background:#e53935;

color:white;

padding:6px 12px;

border-radius:20px;

}

</style>

<script>

let claimID=1;

function addClaim(){

let patient=document.getElementById("insPatient").value;

let company=document.getElementById("insCompany").value;

let policy=document.getElementById("insPolicy").value;

let amount=document.getElementById("insAmount").value;

let status=document.getElementById("insStatus").value;

if(patient==""||company==""||policy==""||amount==""){

alert("Please fill all fields");

return;

}

claimID++;

document.getElementById("totalClaims").innerHTML=claimID+15;

if(status=="Approved"){

document.getElementById("approvedClaims").innerHTML++;

}

if(status=="Pending"){

document.getElementById("pendingClaims").innerHTML++;

}

let badge="<span class='pendingStatus'>Pending</span>";

if(status=="Approved"){

badge="<span class='approvedStatus'>Approved</span>";

}

if(status=="Rejected"){

badge="<span class='rejectedStatus'>Rejected</span>";

}

let row="<tr>"+

"<td>"+claimID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+company+"</td>"+

"<td>"+policy+"</td>"+

"<td>₹"+amount+"</td>"+

"<td>"+badge+"</td>"+

"</tr>";

document.getElementById("insuranceBody").innerHTML+=row;

document.getElementById("insPatient").value="";

document.getElementById("insCompany").value="";

document.getElementById("insPolicy").value="";

document.getElementById("insAmount").value="";

alert("Insurance claim submitted successfully.");

}

</script>
<!-- ================= LIVE SUPPORT MANAGEMENT ================= -->

<section class="supportSection">

<h2 class="title">💬 Live Patient Support</h2>

<div class="supportGrid">

<div class="supportForm">

<input type="text" id="supportName" placeholder="Patient Name">

<input type="email" id="supportEmail" placeholder="Email">

<select id="supportType">

<option>Appointment</option>
<option>Billing</option>
<option>Insurance</option>
<option>Emergency</option>
<option>Laboratory</option>
<option>Pharmacy</option>

</select>

<textarea id="supportMessage"

placeholder="Describe your problem..."

rows="6"></textarea>

<button onclick="submitTicket()">

Submit Ticket

</button>

</div>

<div class="ticketStatus">

<h3>Today's Support</h3>

<div class="statusCard">

<h1 id="openTickets">12</h1>

<p>Open Tickets</p>

</div>

<div class="statusCard">

<h1 id="closedTickets">48</h1>

<p>Closed Tickets</p>

</div>

<div class="statusCard">

<h1 id="onlineAgents">8</h1>

<p>Support Agents Online</p>

</div>

</div>

</div>

<table class="supportTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Category</th>

<th>Email</th>

<th>Status</th>

<th>Priority</th>

</tr>

</thead>

<tbody id="supportBody">

<tr>

<td>1</td>

<td>Mohamed</td>

<td>Appointment</td>

<td>patient@email.com</td>

<td><span class="pending">Pending</span></td>

<td><span class="high">High</span></td>

</tr>

</tbody>

</table>

</section>

<style>

.supportSection{

padding:90px 8%;

background:#eef8ff;

}

.supportGrid{

display:grid;

grid-template-columns:2fr 1fr;

gap:30px;

margin-bottom:35px;

}

.supportForm{

background:white;

padding:30px;

border-radius:20px;

box-shadow:0 12px 25px rgba(0,0,0,.08);

}

.supportForm input,

.supportForm select,

.supportForm textarea{

width:100%;

padding:15px;

margin:10px 0;

border:1px solid #ccc;

border-radius:10px;

}

.supportForm button{

width:100%;

padding:15px;

background:#009688;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-size:17px;

}

.ticketStatus{

display:grid;

gap:20px;

}

.statusCard{

background:white;

padding:25px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.statusCard h1{

font-size:48px;

color:#009688;

}

.supportTable{

width:100%;

background:white;

border-collapse:collapse;

box-shadow:0 10px 20px rgba(0,0,0,.08);

overflow:hidden;

border-radius:15px;

}

.supportTable th{

background:#009688;

color:white;

padding:15px;

}

.supportTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.pending{

background:#ff9800;

color:white;

padding:6px 12px;

border-radius:20px;

}

.high{

background:#e53935;

color:white;

padding:6px 12px;

border-radius:20px;

}

.medium{

background:#2196f3;

color:white;

padding:6px 12px;

border-radius:20px;

}

.low{

background:#4caf50;

color:white;

padding:6px 12px;

border-radius:20px;

}

@media(max-width:900px){

.supportGrid{

grid-template-columns:1fr;

}

}

</style>

<script>

let supportID=1;

function submitTicket(){

let name=document.getElementById("supportName").value;

let email=document.getElementById("supportEmail").value;

let category=document.getElementById("supportType").value;

let message=document.getElementById("supportMessage").value;

if(name==""||email==""||message==""){

alert("Please fill all fields.");

return;

}

supportID++;

let row="<tr>"+

"<td>"+supportID+"</td>"+

"<td>"+name+"</td>"+

"<td>"+category+"</td>"+

"<td>"+email+"</td>"+

"<td><span class='pending'>Pending</span></td>"+

"<td><span class='medium'>Medium</span></td>"+

"</tr>";

document.getElementById("supportBody").innerHTML+=row;

document.getElementById("supportName").value="";

document.getElementById("supportEmail").value="";

document.getElementById("supportMessage").value="";

document.getElementById("openTickets").innerHTML=

parseInt(document.getElementById("openTickets").innerHTML)+1;

alert("🎫 Support ticket submitted successfully.");

}

</script><!-- ================= PRESCRIPTION MANAGEMENT ================= -->

<section class="prescriptionSection">

<h2 class="title">💊 Prescription Management</h2>

<div class="prescriptionForm">

<input type="text" id="presPatient" placeholder="Patient Name">

<input type="text" id="presDoctor" placeholder="Doctor Name">

<input type="text" id="presMedicine" placeholder="Medicine Name">

<input type="text" id="presDosage" placeholder="Dosage (e.g. 1 Tablet Twice Daily)">

<input type="number" id="presDays" placeholder="Days">

<button onclick="addPrescription()">

Save Prescription

</button>

</div>

<table class="prescriptionTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Doctor</th>

<th>Medicine</th>

<th>Dosage</th>

<th>Days</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="prescriptionBody">

<tr>

<td>1</td>

<td>Mohamed</td>

<td>Dr. James</td>

<td>Paracetamol</td>

<td>1 Tablet Morning & Night</td>

<td>5</td>

<td><span class="activePrescription">Active</span></td>

<td>

<button onclick="completePrescription(this)">

Complete

</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.prescriptionSection{

padding:90px 8%;

background:#f9fcff;

}

.prescriptionForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.prescriptionForm input{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.prescriptionForm button{

padding:15px;

background:#009688;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.prescriptionTable{

width:100%;

background:white;

border-collapse:collapse;

border-radius:15px;

overflow:hidden;

box-shadow:0 12px 25px rgba(0,0,0,.08);

}

.prescriptionTable th{

background:#009688;

color:white;

padding:15px;

}

.prescriptionTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.prescriptionTable tr:hover{

background:#f0fffb;

}

.activePrescription{

background:#4caf50;

color:white;

padding:6px 12px;

border-radius:20px;

}

.completedPrescription{

background:#9e9e9e;

color:white;

padding:6px 12px;

border-radius:20px;

}

.prescriptionTable button{

padding:8px 16px;

background:#1976d2;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let prescriptionID=1;

function addPrescription(){

let patient=document.getElementById("presPatient").value;

let doctor=document.getElementById("presDoctor").value;

let medicine=document.getElementById("presMedicine").value;

let dosage=document.getElementById("presDosage").value;

let days=document.getElementById("presDays").value;

if(patient==""||doctor==""||medicine==""||dosage==""||days==""){

alert("Please fill all fields");

return;

}

prescriptionID++;

let row="<tr>"+

"<td>"+prescriptionID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+doctor+"</td>"+

"<td>"+medicine+"</td>"+

"<td>"+dosage+"</td>"+

"<td>"+days+"</td>"+

"<td><span class='activePrescription'>Active</span></td>"+

"<td><button onclick='completePrescription(this)'>Complete</button></td>"+

"</tr>";

document.getElementById("prescriptionBody").innerHTML+=row;

document.getElementById("presPatient").value="";

document.getElementById("presDoctor").value="";

document.getElementById("presMedicine").value="";

document.getElementById("presDosage").value="";

document.getElementById("presDays").value="";

}

function completePrescription(btn){

let row=btn.parentElement.parentElement;

row.cells[6].innerHTML="<span class='completedPrescription'>Completed</span>";

btn.innerHTML="Done";

btn.disabled=true;

}

</script>
<!-- ================= PAYMENT MANAGEMENT ================= -->

<section class="paymentSection">

<h2 class="title">💰 Payment Management</h2>

<div class="paymentForm">

<input type="text" id="payPatient" placeholder="Patient Name">

<input type="text" id="payBill" placeholder="Bill Number">

<input type="number" id="payAmount" placeholder="Amount (₹)">

<select id="payMethod">

<option>Cash</option>
<option>UPI</option>
<option>Credit Card</option>
<option>Debit Card</option>
<option>Net Banking</option>
<option>Insurance</option>

</select>

<button onclick="addPayment()">

Pay Now

</button>

</div>

<div class="paymentCards">

<div class="paymentCard">

<h1 id="todayCollection">₹250000</h1>

<p>Today's Collection</p>

</div>

<div class="paymentCard">

<h1 id="totalTransactions">120</h1>

<p>Total Transactions</p>

</div>

<div class="paymentCard">

<h1 id="pendingPayments">18</h1>

<p>Pending Payments</p>

</div>

</div>

<table class="paymentTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Bill No</th>

<th>Amount</th>

<th>Method</th>

<th>Status</th>

</tr>

</thead>

<tbody id="paymentBody">

<tr>

<td>1</td>

<td>Mohamed</td>

<td>BILL1001</td>

<td>₹5000</td>

<td>UPI</td>

<td><span class="paidStatus">Paid</span></td>

</tr>

</tbody>

</table>

</section>

<style>

.paymentSection{

padding:90px 8%;

background:#f6fff8;

}

.paymentForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.paymentForm input,

.paymentForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.paymentForm button{

padding:15px;

background:#2e7d32;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.paymentCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.paymentCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 25px rgba(0,0,0,.08);

}

.paymentCard h1{

font-size:42px;

color:#2e7d32;

}

.paymentTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 25px rgba(0,0,0,.08);

}

.paymentTable th{

background:#2e7d32;

color:white;

padding:15px;

}

.paymentTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.paymentTable tr:hover{

background:#f0fff4;

}

.paidStatus{

background:#28a745;

color:white;

padding:6px 12px;

border-radius:20px;

}

</style>

<script>

let paymentID=1;

function addPayment(){

let patient=document.getElementById("payPatient").value;

let bill=document.getElementById("payBill").value;

let amount=document.getElementById("payAmount").value;

let method=document.getElementById("payMethod").value;

if(patient==""||bill==""||amount==""){

alert("Please fill all fields");

return;

}

paymentID++;

let row="<tr>"+

"<td>"+paymentID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+bill+"</td>"+

"<td>₹"+amount+"</td>"+

"<td>"+method+"</td>"+

"<td><span class='paidStatus'>Paid</span></td>"+

"</tr>";

document.getElementById("paymentBody").innerHTML+=row;

document.getElementById("payPatient").value="";

document.getElementById("payBill").value="";

document.getElementById("payAmount").value="";

let total=parseInt(document.getElementById("todayCollection").innerHTML.replace("₹",""));

document.getElementById("todayCollection").innerHTML="₹"+(total+parseInt(amount));

document.getElementById("totalTransactions").innerHTML=
parseInt(document.getElementById("totalTransactions").innerHTML)+1;

alert("✅ Payment Successful");

}

</script>
<!-- ================= DOCTOR APPOINTMENT CALENDAR ================= -->

<section class="appointmentSection">

<h2 class="title">📅 Doctor Appointment Calendar</h2>

<div class="appointmentForm">

<input type="text" id="appPatient" placeholder="Patient Name">

<input type="text" id="appDoctor" placeholder="Doctor Name">

<input type="date" id="appDate">

<input type="time" id="appTime">

<select id="appStatus">

<option>Booked</option>
<option>Confirmed</option>
<option>Cancelled</option>

</select>

<button onclick="addAppointment()">

Book Appointment

</button>

</div>

<div class="appointmentCards">

<div class="appointmentCard">

<h1 id="todayAppointments">18</h1>

<p>Today's Appointments</p>

</div>

<div class="appointmentCard">

<h1 id="confirmedAppointments">12</h1>

<p>Confirmed</p>

</div>

<div class="appointmentCard">

<h1 id="cancelledAppointments">2</h1>

<p>Cancelled</p>

</div>

<div class="appointmentCard">

<h1 id="availableDoctors">15</h1>

<p>Doctors Available</p>

</div>

</div>

<table class="appointmentTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Doctor</th>

<th>Date</th>

<th>Time</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="appointmentBody">

<tr>

<td>1</td>

<td>Mohamed</td>

<td>Dr. James</td>

<td>2026-08-05</td>

<td>10:00 AM</td>

<td><span class="booked">Booked</span></td>

<td>

<button onclick="confirmAppointment(this)">Confirm</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.appointmentSection{

padding:90px 8%;

background:#f5fbff;

}

.appointmentForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.appointmentForm input,

.appointmentForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.appointmentForm button{

padding:15px;

background:#3f51b5;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.appointmentCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.appointmentCard{

background:white;

padding:30px;

text-align:center;

border-radius:18px;

box-shadow:0 10px 25px rgba(0,0,0,.08);

}

.appointmentCard h1{

font-size:46px;

color:#3f51b5;

}

.appointmentTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 25px rgba(0,0,0,.08);

}

.appointmentTable th{

background:#3f51b5;

color:white;

padding:15px;

}

.appointmentTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.booked{

background:#ff9800;

color:white;

padding:6px 12px;

border-radius:20px;

}

.confirmed{

background:#28a745;

color:white;

padding:6px 12px;

border-radius:20px;

}

.cancelled{

background:#e53935;

color:white;

padding:6px 12px;

border-radius:20px;

}

.appointmentTable button{

padding:8px 16px;

background:#3f51b5;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let appointmentID=1;

function addAppointment(){

let patient=document.getElementById("appPatient").value;

let doctor=document.getElementById("appDoctor").value;

let date=document.getElementById("appDate").value;

let time=document.getElementById("appTime").value;

let status=document.getElementById("appStatus").value;

if(patient==""||doctor==""||date==""||time==""){

alert("Please fill all fields");

return;

}

appointmentID++;

let badge="<span class='booked'>Booked</span>";

if(status=="Confirmed"){

badge="<span class='confirmed'>Confirmed</span>";

}

if(status=="Cancelled"){

badge="<span class='cancelled'>Cancelled</span>";

}

let action=(status=="Booked")

? "<button onclick='confirmAppointment(this)'>Confirm</button>"

: "-";

let row="<tr>"+

"<td>"+appointmentID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+doctor+"</td>"+

"<td>"+date+"</td>"+

"<td>"+time+"</td>"+

"<td>"+badge+"</td>"+

"<td>"+action+"</td>"+

"</tr>";

document.getElementById("appointmentBody").innerHTML+=row;

document.getElementById("todayAppointments").innerHTML=

parseInt(document.getElementById("todayAppointments").innerHTML)+1;

document.getElementById("appPatient").value="";

document.getElementById("appDoctor").value="";

document.getElementById("appDate").value="";

document.getElementById("appTime").value="";

}

function confirmAppointment(btn){

let row=btn.parentElement.parentElement;

row.cells[5].innerHTML="<span class='confirmed'>Confirmed</span>";

btn.innerHTML="Confirmed";

btn.disabled=true;

document.getElementById("confirmedAppointments").innerHTML=

parseInt(document.getElementById("confirmedAppointments").innerHTML)+1;

}

</script>
<!-- ================= ROOM & WARD MANAGEMENT ================= -->

<section class="roomSection">

<h2 class="title">🏨 Room & Ward Management</h2>

<div class="roomForm">

<input type="text" id="roomPatient" placeholder="Patient Name">

<select id="roomWard">

<option>General Ward</option>
<option>Private Room</option>
<option>Semi Private</option>
<option>Deluxe Room</option>
<option>ICU</option>
<option>VIP Suite</option>

</select>

<input type="text" id="roomNumber" placeholder="Room Number">

<input type="number" id="roomCharge" placeholder="Charge Per Day (₹)">

<button onclick="assignRoom()">

Assign Room

</button>

</div>

<div class="roomCards">

<div class="roomCard">

<h1 id="totalRooms">100</h1>

<p>Total Rooms</p>

</div>

<div class="roomCard">

<h1 id="availableRooms">75</h1>

<p>Available</p>

</div>

<div class="roomCard">

<h1 id="occupiedRooms">25</h1>

<p>Occupied</p>

</div>

<div class="roomCard">

<h1 id="maintenanceRooms">5</h1>

<p>Maintenance</p>

</div>

</div>

<table class="roomTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Ward</th>

<th>Room No</th>

<th>Charge/Day</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="roomBody">

<tr>

<td>1</td>

<td>Mohamed</td>

<td>Private Room</td>

<td>P-101</td>

<td>₹2500</td>

<td><span class="occupied">Occupied</span></td>

<td>

<button onclick="dischargeRoom(this)">Discharge</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.roomSection{

padding:90px 8%;

background:#f7fbff;

}

.roomForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.roomForm input,
.roomForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.roomForm button{

padding:15px;

background:#00695c;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.roomCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.roomCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.roomCard h1{

font-size:45px;

color:#00695c;

}

.roomTable{

width:100%;

background:white;

border-collapse:collapse;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.roomTable th{

background:#00695c;

color:white;

padding:15px;

}

.roomTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.roomTable tr:hover{

background:#f0fff9;

}

.occupied{

background:#4caf50;

color:white;

padding:6px 12px;

border-radius:20px;

}

.available{

background:#2196f3;

color:white;

padding:6px 12px;

border-radius:20px;

}

.roomTable button{

padding:8px 18px;

background:#d32f2f;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let roomID=1;

let availableRoomCount=75;

let occupiedRoomCount=25;

function assignRoom(){

let patient=document.getElementById("roomPatient").value;

let ward=document.getElementById("roomWard").value;

let room=document.getElementById("roomNumber").value;

let charge=document.getElementById("roomCharge").value;

if(patient==""||room==""||charge==""){

alert("Please fill all fields");

return;

}

roomID++;

availableRoomCount--;

occupiedRoomCount++;

document.getElementById("availableRooms").innerHTML=availableRoomCount;

document.getElementById("occupiedRooms").innerHTML=occupiedRoomCount;

let row="<tr>"+

"<td>"+roomID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+ward+"</td>"+

"<td>"+room+"</td>"+

"<td>₹"+charge+"</td>"+

"<td><span class='occupied'>Occupied</span></td>"+

"<td><button onclick='dischargeRoom(this)'>Discharge</button></td>"+

"</tr>";

document.getElementById("roomBody").innerHTML+=row;

document.getElementById("roomPatient").value="";

document.getElementById("roomNumber").value="";

document.getElementById("roomCharge").value="";

}

function dischargeRoom(btn){

let row=btn.parentElement.parentElement;

row.cells[5].innerHTML="<span class='available'>Available</span>";

btn.innerHTML="Completed";

btn.disabled=true;

availableRoomCount++;

occupiedRoomCount--;

document.getElementById("availableRooms").innerHTML=availableRoomCount;

document.getElementById("occupiedRooms").innerHTML=occupiedRoomCount;

}

</script>
<!-- ================= EMERGENCY MANAGEMENT ================= -->

<section class="erSection">

<h2 class="title">🚑 Emergency (ER) Management</h2>

<div class="erForm">

<input type="text" id="erPatient" placeholder="Patient Name">

<input type="number" id="erAge" placeholder="Age">

<select id="erPriority">

<option>Critical</option>
<option>High</option>
<option>Medium</option>
<option>Low</option>

</select>

<input type="text" id="erDoctor" placeholder="Doctor Assigned">

<input type="text" id="erBed" placeholder="Emergency Bed No">

<button onclick="addEmergency()">

Admit Emergency

</button>

</div>

<div class="erCards">

<div class="erCard">

<h1 id="totalEmergency">40</h1>

<p>Total Cases</p>

</div>

<div class="erCard">

<h1 id="criticalCases">8</h1>

<p>Critical</p>

</div>

<div class="erCard">

<h1 id="availableERBeds">12</h1>

<p>Available Beds</p>

</div>

<div class="erCard">

<h1 id="ambulanceArrivals">25</h1>

<p>Ambulance Arrivals</p>

</div>

</div>

<table class="erTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Age</th>

<th>Priority</th>

<th>Doctor</th>

<th>Bed</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="erBody">

<tr>

<td>1</td>

<td>Mohamed</td>

<td>20</td>

<td><span class="critical">Critical</span></td>

<td>Dr. Kumar</td>

<td>E-01</td>

<td><span class="treatment">Under Treatment</span></td>

<td>

<button onclick="dischargeER(this)">

Discharge

</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.erSection{

padding:90px 8%;

background:#fff5f5;

}

.erForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.erForm input,

.erForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.erForm button{

padding:15px;

background:#d32f2f;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.erCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.erCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.erCard h1{

font-size:46px;

color:#d32f2f;

}

.erTable{

width:100%;

background:white;

border-collapse:collapse;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.erTable th{

background:#d32f2f;

color:white;

padding:15px;

}

.erTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.critical{

background:#d50000;

color:white;

padding:6px 12px;

border-radius:20px;

}

.high{

background:#ff6f00;

color:white;

padding:6px 12px;

border-radius:20px;

}

.medium{

background:#1976d2;

color:white;

padding:6px 12px;

border-radius:20px;

}

.low{

background:#388e3c;

color:white;

padding:6px 12px;

border-radius:20px;

}

.treatment{

background:#7b1fa2;

color:white;

padding:6px 12px;

border-radius:20px;

}

.discharged{

background:#4caf50;

color:white;

padding:6px 12px;

border-radius:20px;

}

.erTable button{

padding:8px 18px;

background:#d32f2f;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let erID=1;

let availableBeds=12;

function addEmergency(){

let patient=document.getElementById("erPatient").value;

let age=document.getElementById("erAge").value;

let priority=document.getElementById("erPriority").value;

let doctor=document.getElementById("erDoctor").value;

let bed=document.getElementById("erBed").value;

if(patient==""||age==""||doctor==""||bed==""){

alert("Please fill all fields");

return;

}

erID++;

availableBeds--;

document.getElementById("availableERBeds").innerHTML=availableBeds;

if(priority=="Critical"){

document.getElementById("criticalCases").innerHTML=
parseInt(document.getElementById("criticalCases").innerHTML)+1;

}

let badge="<span class='low'>Low</span>";

if(priority=="Critical") badge="<span class='critical'>Critical</span>";

if(priority=="High") badge="<span class='high'>High</span>";

if(priority=="Medium") badge="<span class='medium'>Medium</span>";

let row="<tr>"+

"<td>"+erID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+age+"</td>"+

"<td>"+badge+"</td>"+

"<td>"+doctor+"</td>"+

"<td>"+bed+"</td>"+

"<td><span class='treatment'>Under Treatment</span></td>"+

"<td><button onclick='dischargeER(this)'>Discharge</button></td>"+

"</tr>";

document.getElementById("erBody").innerHTML+=row;

document.getElementById("totalEmergency").innerHTML=
parseInt(document.getElementById("totalEmergency").innerHTML)+1;

document.getElementById("erPatient").value="";

document.getElementById("erAge").value="";

document.getElementById("erDoctor").value="";

document.getElementById("erBed").value="";

alert("🚑 Emergency patient admitted successfully.");

}

function dischargeER(btn){

let row=btn.parentElement.parentElement;

row.cells[6].innerHTML="<span class='discharged'>Discharged</span>";

btn.innerHTML="Completed";

btn.disabled=true;

availableBeds++;

document.getElementById("availableERBeds").innerHTML=availableBeds;

}

</script>
<!-- ================= MATERNITY & NEWBORN MANAGEMENT ================= -->

<section class="maternitySection">

<h2 class="title">👶 Maternity & Newborn Management</h2>

<div class="maternityForm">

<input type="text" id="motherName" placeholder="Mother Name">

<input type="number" id="motherAge" placeholder="Mother Age">

<input type="text" id="doctorName" placeholder="Gynecologist">

<input type="date" id="deliveryDate">

<select id="deliveryType">

<option>Normal Delivery</option>
<option>C-Section</option>
<option>Forceps Delivery</option>
<option>Vacuum Delivery</option>

</select>

<input type="text" id="babyName" placeholder="Baby Name">

<select id="babyGender">

<option>Male</option>
<option>Female</option>

</select>

<input type="number" id="babyWeight" placeholder="Weight (kg)">

<button onclick="addDelivery()">

Register Delivery

</button>

</div>

<div class="maternityCards">

<div class="maternityCard">

<h1 id="todayBirths">12</h1>

<p>Today's Births</p>

</div>

<div class="maternityCard">

<h1 id="normalDelivery">7</h1>

<p>Normal Delivery</p>

</div>

<div class="maternityCard">

<h1 id="cSectionCount">5</h1>

<p>C-Section</p>

</div>

<div class="maternityCard">

<h1 id="nicuBabies">3</h1>

<p>NICU Babies</p>

</div>

</div>

<table class="maternityTable">

<thead>

<tr>

<th>ID</th>

<th>Mother</th>

<th>Baby</th>

<th>Gender</th>

<th>Weight</th>

<th>Doctor</th>

<th>Delivery</th>

<th>Status</th>

</tr>

</thead>

<tbody id="maternityBody">

<tr>

<td>1</td>

<td>Aisha</td>

<td>Baby Ahmed</td>

<td>Male</td>

<td>3.2 kg</td>

<td>Dr. Priya</td>

<td>Normal Delivery</td>

<td><span class="healthy">Healthy</span></td>

</tr>

</tbody>

</table>

</section>

<style>

.maternitySection{

padding:90px 8%;

background:#fff8fb;

}

.maternityForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.maternityForm input,

.maternityForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.maternityForm button{

padding:15px;

background:#e91e63;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.maternityCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.maternityCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.maternityCard h1{

font-size:45px;

color:#e91e63;

}

.maternityTable{

width:100%;

background:white;

border-collapse:collapse;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.maternityTable th{

background:#e91e63;

color:white;

padding:15px;

}

.maternityTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.healthy{

background:#4caf50;

color:white;

padding:6px 12px;

border-radius:20px;

}

.nicustatus{

background:#ff9800;

color:white;

padding:6px 12px;

border-radius:20px;

}

</style>

<script>

let maternityID=1;

function addDelivery(){

let mother=document.getElementById("motherName").value;

let age=document.getElementById("motherAge").value;

let doctor=document.getElementById("doctorName").value;

let date=document.getElementById("deliveryDate").value;

let delivery=document.getElementById("deliveryType").value;

let baby=document.getElementById("babyName").value;

let gender=document.getElementById("babyGender").value;

let weight=document.getElementById("babyWeight").value;

if(mother==""||doctor==""||date==""||baby==""||weight==""){

alert("Please fill all fields");

return;

}

maternityID++;

if(delivery=="Normal Delivery"){

document.getElementById("normalDelivery").innerHTML=
parseInt(document.getElementById("normalDelivery").innerHTML)+1;

}

if(delivery=="C-Section"){

document.getElementById("cSectionCount").innerHTML=
parseInt(document.getElementById("cSectionCount").innerHTML)+1;

}

document.getElementById("todayBirths").innerHTML=
parseInt(document.getElementById("todayBirths").innerHTML)+1;

let row="<tr>"+

"<td>"+maternityID+"</td>"+

"<td>"+mother+"</td>"+

"<td>"+baby+"</td>"+

"<td>"+gender+"</td>"+

"<td>"+weight+" kg</td>"+

"<td>"+doctor+"</td>"+

"<td>"+delivery+"</td>"+

"<td><span class='healthy'>Healthy</span></td>"+

"</tr>";

document.getElementById("maternityBody").innerHTML+=row;

document.getElementById("motherName").value="";

document.getElementById("motherAge").value="";

document.getElementById("doctorName").value="";

document.getElementById("deliveryDate").value="";

document.getElementById("babyName").value="";

document.getElementById("babyWeight").value="";

alert("👶 Delivery registered successfully.");

}

</script>
<!-- ================= ELECTRONIC MEDICAL RECORDS ================= -->

<section class="emrSection">

<h2 class="title">🧠 Electronic Medical Records (EMR)</h2>

<div class="emrForm">

<input type="text" id="emrPatient" placeholder="Patient Name">

<input type="number" id="emrAge" placeholder="Age">

<select id="emrGender">

<option>Male</option>
<option>Female</option>
<option>Other</option>

</select>

<input type="text" id="emrDoctor" placeholder="Doctor Name">

<textarea id="emrDiagnosis" placeholder="Diagnosis"></textarea>

<textarea id="emrAllergy" placeholder="Allergies"></textarea>

<textarea id="emrMedicine" placeholder="Prescribed Medicines"></textarea>

<textarea id="emrHistory" placeholder="Past Medical History"></textarea>

<button onclick="saveEMR()">

Save Medical Record

</button>

</div>

<div class="emrCards">

<div class="emrCard">

<h1 id="recordCount">500</h1>

<p>Total Records</p>

</div>

<div class="emrCard">

<h1 id="todayRecords">18</h1>

<p>Today's Records</p>

</div>

<div class="emrCard">

<h1 id="criticalPatients">9</h1>

<p>Critical Patients</p>

</div>

<div class="emrCard">

<h1 id="followupPatients">24</h1>

<p>Follow-Up Due</p>

</div>

</div>

<table class="emrTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Age</th>

<th>Doctor</th>

<th>Diagnosis</th>

<th>Medicines</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="emrBody">

<tr>

<td>1</td>

<td>Mohamed</td>

<td>20</td>

<td>Dr. Kumar</td>

<td>Viral Fever</td>

<td>Paracetamol</td>

<td><span class="activeRecord">Active</span></td>

<td>

<button onclick="viewRecord(this)">

View

</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.emrSection{

padding:90px 8%;

background:#f4fbff;

}

.emrForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(250px,1fr));

gap:15px;

margin-bottom:30px;

}

.emrForm input,

.emrForm select,

.emrForm textarea{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

resize:none;

}

.emrForm textarea{

min-height:90px;

}

.emrForm button{

padding:15px;

background:#1565c0;

color:white;

border:none;

border-radius:10px;

font-size:16px;

cursor:pointer;

font-weight:bold;

}

.emrCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.emrCard{

background:white;

padding:30px;

border-radius:20px;

text-align:center;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.emrCard h1{

font-size:45px;

color:#1565c0;

}

.emrTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.emrTable th{

background:#1565c0;

color:white;

padding:15px;

}

.emrTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.activeRecord{

background:#4caf50;

color:white;

padding:6px 12px;

border-radius:20px;

}

.emrTable button{

padding:8px 18px;

background:#1565c0;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let emrID=1;

function saveEMR(){

let patient=document.getElementById("emrPatient").value;

let age=document.getElementById("emrAge").value;

let doctor=document.getElementById("emrDoctor").value;

let diagnosis=document.getElementById("emrDiagnosis").value;

let medicine=document.getElementById("emrMedicine").value;

if(patient==""||age==""||doctor==""||diagnosis==""){

alert("Please fill all required fields");

return;

}

emrID++;

document.getElementById("recordCount").innerHTML=
parseInt(document.getElementById("recordCount").innerHTML)+1;

document.getElementById("todayRecords").innerHTML=
parseInt(document.getElementById("todayRecords").innerHTML)+1;

let row="<tr>"+

"<td>"+emrID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+age+"</td>"+

"<td>"+doctor+"</td>"+

"<td>"+diagnosis+"</td>"+

"<td>"+medicine+"</td>"+

"<td><span class='activeRecord'>Active</span></td>"+

"<td><button onclick='viewRecord(this)'>View</button></td>"+

"</tr>";

document.getElementById("emrBody").innerHTML+=row;

document.getElementById("emrPatient").value="";

document.getElementById("emrAge").value="";

document.getElementById("emrDoctor").value="";

document.getElementById("emrDiagnosis").value="";

document.getElementById("emrAllergy").value="";

document.getElementById("emrMedicine").value="";

document.getElementById("emrHistory").value="";

alert("✅ Medical Record Saved Successfully");

}

function viewRecord(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+

"\nAge : "+row.cells[2].innerHTML+

"\nDoctor : "+row.cells[3].innerHTML+

"\nDiagnosis : "+row.cells[4].innerHTML+

"\nMedicine : "+row.cells[5].innerHTML

);

}

</script>
<!-- ================= HOSPITAL ANALYTICS DASHBOARD ================= -->

<section class="analyticsSection">

<h2 class="title">📈 Hospital Analytics Dashboard</h2>

<div class="analyticsCards">

<div class="analyticsCard">
<h1 id="totalRevenue">₹12,50,000</h1>
<p>Total Revenue</p>
</div>

<div class="analyticsCard">
<h1 id="totalPatients">1,280</h1>
<p>Total Patients</p>
</div>

<div class="analyticsCard">
<h1 id="todayAppointmentsDash">82</h1>
<p>Today's Appointments</p>
</div>

<div class="analyticsCard">
<h1 id="bedOccupancy">78%</h1>
<p>Bed Occupancy</p>
</div>

<div class="analyticsCard">
<h1 id="surgeriesDone">35</h1>
<p>Surgeries</p>
</div>

<div class="analyticsCard">
<h1 id="medicineSales">₹3,25,000</h1>
<p>Pharmacy Sales</p>
</div>

</div>

<div class="chartContainer">

<div class="chartBox">

<h3>Monthly Revenue</h3>

<div class="barChart">

<div class="bar" style="height:90%;">
<span>Jan</span>
</div>

<div class="bar" style="height:60%;">
<span>Feb</span>
</div>

<div class="bar" style="height:70%;">
<span>Mar</span>
</div>

<div class="bar" style="height:95%;">
<span>Apr</span>
</div>

<div class="bar" style="height:80%;">
<span>May</span>
</div>

<div class="bar" style="height:100%;">
<span>Jun</span>
</div>

</div>

</div>

<div class="chartBox">

<h3>Doctor Performance</h3>

<table class="performanceTable">

<tr>

<th>Doctor</th>

<th>Patients</th>

<th>Rating</th>

</tr>

<tr>

<td>Dr. Kumar</td>

<td>210</td>

<td>⭐⭐⭐⭐⭐</td>

</tr>

<tr>

<td>Dr. Priya</td>

<td>184</td>

<td>⭐⭐⭐⭐⭐</td>

</tr>

<tr>

<td>Dr. James</td>

<td>168</td>

<td>⭐⭐⭐⭐</td>

</tr>

<tr>

<td>Dr. Ahmed</td>

<td>142</td>

<td>⭐⭐⭐⭐</td>

</tr>

</table>

</div>

</div>

</section>

<style>

.analyticsSection{

padding:90px 8%;

background:#f4faff;

}

.analyticsCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:35px;

}

.analyticsCard{

background:white;

padding:30px;

border-radius:20px;

text-align:center;

box-shadow:0 10px 20px rgba(0,0,0,.08);

transition:.3s;

}

.analyticsCard:hover{

transform:translateY(-8px);

}

.analyticsCard h1{

color:#0d6efd;

font-size:42px;

}

.chartContainer{

display:grid;

grid-template-columns:1fr 1fr;

gap:30px;

}

.chartBox{

background:white;

padding:25px;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.barChart{

display:flex;

justify-content:space-around;

align-items:flex-end;

height:320px;

margin-top:20px;

}

.bar{

width:45px;

background:#0d6efd;

border-radius:10px 10px 0 0;

position:relative;

transition:.4s;

cursor:pointer;

}

.bar:hover{

background:#28a745;

transform:scaleY(1.05);

}

.bar span{

position:absolute;

bottom:-30px;

left:50%;

transform:translateX(-50%);

font-weight:bold;

}

.performanceTable{

width:100%;

border-collapse:collapse;

margin-top:20px;

}

.performanceTable th{

background:#0d6efd;

color:white;

padding:12px;

}

.performanceTable td{

padding:12px;

text-align:center;

border-bottom:1px solid #ddd;

}

.performanceTable tr:hover{

background:#f7f7f7;

}

@media(max-width:900px){

.chartContainer{

grid-template-columns:1fr;

}

}

</style>

<script>

setInterval(function(){

let revenue=Math.floor(Math.random()*40000)+1200000;

document.getElementById("totalRevenue").innerHTML="₹"+revenue.toLocaleString();

let patients=Math.floor(Math.random()*100)+1250;

document.getElementById("totalPatients").innerHTML=patients;

let appointments=Math.floor(Math.random()*20)+70;

document.getElementById("todayAppointmentsDash").innerHTML=appointments;

let occupancy=Math.floor(Math.random()*20)+70;

document.getElementById("bedOccupancy").innerHTML=occupancy+"%";

let surgeries=Math.floor(Math.random()*10)+30;

document.getElementById("surgeriesDone").innerHTML=surgeries;

let sales=Math.floor(Math.random()*60000)+300000;

document.getElementById("medicineSales").innerHTML="₹"+sales.toLocaleString();

},5000);

</script>
<!-- ================= ROLE BASED LOGIN ================= -->

<section class="roleSection">

<h2 class="title">🔐 Role-Based Login & Access Control</h2>

<div class="loginCard">

<h3>Hospital Staff Login</h3>

<input type="text" id="roleUsername" placeholder="Username">

<input type="password" id="rolePassword" placeholder="Password">

<select id="userRole">

<option>Admin</option>
<option>Doctor</option>
<option>Nurse</option>
<option>Receptionist</option>
<option>Pharmacist</option>
<option>Lab Technician</option>
<option>Accountant</option>
<option>Patient</option>

</select>

<button onclick="loginUser()">

Login

</button>

</div>

<div class="permissionBox">

<h3>Role Permissions</h3>

<ul id="permissionList">

<li>Select a role and login.</li>

</ul>

</div>

</section>

<style>

.roleSection{

padding:90px 8%;

background:#f8fbff;

display:grid;

grid-template-columns:1fr 1fr;

gap:30px;

}

.loginCard{

background:white;

padding:35px;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.loginCard input,

.loginCard select{

width:100%;

padding:15px;

margin:12px 0;

border:1px solid #ccc;

border-radius:10px;

}

.loginCard button{

width:100%;

padding:15px;

background:#673ab7;

color:white;

border:none;

border-radius:10px;

font-size:17px;

cursor:pointer;

font-weight:bold;

}

.permissionBox{

background:white;

padding:35px;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.permissionBox ul{

margin-top:20px;

line-height:35px;

}

.permissionBox li{

font-size:16px;

}

@media(max-width:900px){

.roleSection{

grid-template-columns:1fr;

}

}

</style>

<script>

function loginUser(){

let username=document.getElementById("roleUsername").value;

let password=document.getElementById("rolePassword").value;

let role=document.getElementById("userRole").value;

if(username==""||password==""){

alert("Enter username and password");

return;

}

let permissions=[];

if(role=="Admin"){

permissions=[

"Manage all hospital modules",

"View reports",

"Manage users",

"Financial management",

"System settings"

];

}

if(role=="Doctor"){

permissions=[

"View appointments",

"Manage prescriptions",

"Update EMR",

"View laboratory reports",

"Discharge patients"

];

}

if(role=="Nurse"){

permissions=[

"Patient monitoring",

"Update vital signs",

"Vaccination",

"Medicine administration"

];

}

if(role=="Receptionist"){

permissions=[

"Patient registration",

"Appointment booking",

"Billing",

"Room allocation"

];

}

if(role=="Pharmacist"){

permissions=[

"Medicine inventory",

"Dispense medicines",

"Stock updates"

];

}

if(role=="Lab Technician"){

permissions=[

"Upload reports",

"Manage laboratory",

"Update test results"

];

}

if(role=="Accountant"){

permissions=[

"Payments",

"Insurance",

"Revenue reports",

"Expenses"

];

}

if(role=="Patient"){

permissions=[

"View appointments",

"Download reports",

"View prescriptions",

"Pay bills"

];

}

let html="";

for(let i=0;i<permissions.length;i++){

html+="<li>✅ "+permissions[i]+"</li>";

}

document.getElementById("permissionList").innerHTML=html;

alert(role+" Login Successful");

}

</script><!-- ================= MEDICAL EQUIPMENT MANAGEMENT ================= -->

<section class="assetSection">

<h2 class="title">📦 Medical Equipment & Asset Management</h2>

<div class="assetForm">

<input type="text" id="assetName" placeholder="Equipment Name">

<input type="text" id="assetCode" placeholder="Asset Code">

<select id="assetCategory">

<option>MRI Machine</option>
<option>CT Scanner</option>
<option>X-Ray Machine</option>
<option>ECG Machine</option>
<option>Ventilator</option>
<option>Ultrasound</option>
<option>Defibrillator</option>
<option>Patient Monitor</option>

</select>

<input type="date" id="purchaseDate">

<input type="date" id="serviceDate">

<select id="assetStatus">

<option>Available</option>
<option>In Use</option>
<option>Maintenance</option>
<option>Out of Service</option>

</select>

<button onclick="addAsset()">

Add Equipment

</button>

</div>

<div class="assetCards">

<div class="assetCard">

<h1 id="totalAssets">320</h1>

<p>Total Equipment</p>

</div>

<div class="assetCard">

<h1 id="availableAssets">250</h1>

<p>Available</p>

</div>

<div class="assetCard">

<h1 id="maintenanceAssets">18</h1>

<p>Maintenance</p>

</div>

<div class="assetCard">

<h1 id="serviceDue">9</h1>

<p>Service Due</p>

</div>

</div>

<table class="assetTable">

<thead>

<tr>

<th>ID</th>

<th>Equipment</th>

<th>Code</th>

<th>Category</th>

<th>Purchase</th>

<th>Next Service</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="assetBody">

<tr>

<td>1</td>

<td>MRI Scanner</td>

<td>AST-1001</td>

<td>MRI Machine</td>

<td>2025-02-10</td>

<td>2026-08-15</td>

<td><span class="availableAsset">Available</span></td>

<td>

<button onclick="serviceAsset(this)">

Service

</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.assetSection{

padding:90px 8%;

background:#f7fbff;

}

.assetForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.assetForm input,

.assetForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.assetForm button{

padding:15px;

background:#0b7285;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.assetCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.assetCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.assetCard h1{

font-size:45px;

color:#0b7285;

}

.assetTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.assetTable th{

background:#0b7285;

color:white;

padding:15px;

}

.assetTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.assetTable tr:hover{

background:#eefcff;

}

.availableAsset{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.inUseAsset{

background:#1565c0;

color:white;

padding:6px 12px;

border-radius:20px;

}

.maintenanceAsset{

background:#ff9800;

color:white;

padding:6px 12px;

border-radius:20px;

}

.outServiceAsset{

background:#d32f2f;

color:white;

padding:6px 12px;

border-radius:20px;

}

.assetTable button{

padding:8px 18px;

background:#0b7285;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let assetID=1;

function addAsset(){

let name=document.getElementById("assetName").value;

let code=document.getElementById("assetCode").value;

let category=document.getElementById("assetCategory").value;

let purchase=document.getElementById("purchaseDate").value;

let service=document.getElementById("serviceDate").value;

let status=document.getElementById("assetStatus").value;

if(name==""||code==""||purchase==""||service==""){

alert("Please fill all fields");

return;

}

assetID++;

document.getElementById("totalAssets").innerHTML=
parseInt(document.getElementById("totalAssets").innerHTML)+1;

let badge="<span class='availableAsset'>Available</span>";

if(status=="In Use") badge="<span class='inUseAsset'>In Use</span>";

if(status=="Maintenance") badge="<span class='maintenanceAsset'>Maintenance</span>";

if(status=="Out of Service") badge="<span class='outServiceAsset'>Out of Service</span>";

let row="<tr>"+

"<td>"+assetID+"</td>"+

"<td>"+name+"</td>"+

"<td>"+code+"</td>"+

"<td>"+category+"</td>"+

"<td>"+purchase+"</td>"+

"<td>"+service+"</td>"+

"<td>"+badge+"</td>"+

"<td><button onclick='serviceAsset(this)'>Service</button></td>"+

"</tr>";

document.getElementById("assetBody").innerHTML+=row;

document.getElementById("assetName").value="";

document.getElementById("assetCode").value="";

document.getElementById("purchaseDate").value="";

document.getElementById("serviceDate").value="";

alert("📦 Equipment added successfully.");

}

function serviceAsset(btn){

let row=btn.parentElement.parentElement;

row.cells[6].innerHTML="<span class='maintenanceAsset'>Maintenance</span>";

btn.innerHTML="Servicing";

btn.disabled=true;

}

</script>
<!-- ================= HR & EMPLOYEE ATTENDANCE ================= -->

<section class="hrSection">

<h2 class="title">👨‍💼 HR & Employee Attendance</h2>

<div class="hrForm">

<input type="text" id="empName" placeholder="Employee Name">

<input type="text" id="empId" placeholder="Employee ID">

<select id="empDepartment">

<option>Doctor</option>
<option>Nurse</option>
<option>Reception</option>
<option>Laboratory</option>
<option>Pharmacy</option>
<option>Accounts</option>
<option>Administration</option>

</select>

<select id="empShift">

<option>Morning</option>
<option>Evening</option>
<option>Night</option>

</select>

<select id="empAttendance">

<option>Present</option>
<option>Absent</option>
<option>Late</option>
<option>Leave</option>

</select>

<button onclick="markAttendance()">

Mark Attendance

</button>

</div>

<div class="hrCards">

<div class="hrCard">

<h1 id="totalEmployees">250</h1>

<p>Total Employees</p>

</div>

<div class="hrCard">

<h1 id="presentEmployees">220</h1>

<p>Present</p>

</div>

<div class="hrCard">

<h1 id="absentEmployees">18</h1>

<p>Absent</p>

</div>

<div class="hrCard">

<h1 id="lateEmployees">12</h1>

<p>Late</p>

</div>

</div>

<table class="hrTable">

<thead>

<tr>

<th>ID</th>

<th>Employee</th>

<th>Employee ID</th>

<th>Department</th>

<th>Shift</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="hrBody">

<tr>

<td>1</td>

<td>Priya</td>

<td>EMP001</td>

<td>Nurse</td>

<td>Morning</td>

<td><span class="present">Present</span></td>

<td>

<button onclick="viewEmployee(this)">

View

</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.hrSection{

padding:90px 8%;

background:#f5f9ff;

}

.hrForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.hrForm input,

.hrForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.hrForm button{

padding:15px;

background:#6a1b9a;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.hrCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.hrCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.hrCard h1{

font-size:45px;

color:#6a1b9a;

}

.hrTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.hrTable th{

background:#6a1b9a;

color:white;

padding:15px;

}

.hrTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.present{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.absent{

background:#d32f2f;

color:white;

padding:6px 12px;

border-radius:20px;

}

.late{

background:#fb8c00;

color:white;

padding:6px 12px;

border-radius:20px;

}

.leave{

background:#1565c0;

color:white;

padding:6px 12px;

border-radius:20px;

}

.hrTable button{

padding:8px 18px;

background:#6a1b9a;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let employeeRecordID=1;

function markAttendance(){

let name=document.getElementById("empName").value;

let empid=document.getElementById("empId").value;

let dept=document.getElementById("empDepartment").value;

let shift=document.getElementById("empShift").value;

let status=document.getElementById("empAttendance").value;

if(name==""||empid==""){

alert("Please fill all fields");

return;

}

employeeRecordID++;

let badge="<span class='present'>Present</span>";

if(status=="Absent"){

badge="<span class='absent'>Absent</span>";

document.getElementById("absentEmployees").innerHTML=

parseInt(document.getElementById("absentEmployees").innerHTML)+1;

}

if(status=="Late"){

badge="<span class='late'>Late</span>";

document.getElementById("lateEmployees").innerHTML=

parseInt(document.getElementById("lateEmployees").innerHTML)+1;

}

if(status=="Leave"){

badge="<span class='leave'>Leave</span>";

}

if(status=="Present"){

document.getElementById("presentEmployees").innerHTML=

parseInt(document.getElementById("presentEmployees").innerHTML)+1;

}

let row="<tr>"+

"<td>"+employeeRecordID+"</td>"+

"<td>"+name+"</td>"+

"<td>"+empid+"</td>"+

"<td>"+dept+"</td>"+

"<td>"+shift+"</td>"+

"<td>"+badge+"</td>"+

"<td><button onclick='viewEmployee(this)'>View</button></td>"+

"</tr>";

document.getElementById("hrBody").innerHTML+=row;

document.getElementById("empName").value="";

document.getElementById("empId").value="";

alert("✅ Attendance marked successfully.");

}

function viewEmployee(btn){

let row=btn.parentElement.parentElement;

alert(

"Employee: "+row.cells[1].innerHTML+

"\nEmployee ID: "+row.cells[2].innerHTML+

"\nDepartment: "+row.cells[3].innerHTML+

"\nShift: "+row.cells[4].innerHTML+

"\nStatus: "+row.cells[5].innerText

);

}

</script>
<!-- ================= PAYROLL MANAGEMENT ================= -->

<section class="payrollSection">

<h2 class="title">💵 Payroll & Salary Management</h2>

<div class="payrollForm">

<input type="text" id="salaryEmployee" placeholder="Employee Name">

<input type="text" id="salaryID" placeholder="Employee ID">

<select id="salaryDepartment">

<option>Doctor</option>
<option>Nurse</option>
<option>Receptionist</option>
<option>Laboratory</option>
<option>Pharmacy</option>
<option>Administration</option>

</select>

<input type="number" id="basicSalary" placeholder="Basic Salary (₹)">

<input type="number" id="allowance" placeholder="Allowance (₹)">

<input type="number" id="deduction" placeholder="Deduction (₹)">

<button onclick="generateSalary()">

Generate Salary

</button>

</div>

<div class="payrollCards">

<div class="payrollCard">

<h1 id="totalPayroll">₹15,00,000</h1>

<p>Monthly Payroll</p>

</div>

<div class="payrollCard">

<h1 id="employeesPaid">185</h1>

<p>Employees Paid</p>

</div>

<div class="payrollCard">

<h1 id="pendingSalary">12</h1>

<p>Pending Salary</p>

</div>

<div class="payrollCard">

<h1 id="averageSalary">₹48,000</h1>

<p>Average Salary</p>

</div>

</div>

<table class="payrollTable">

<thead>

<tr>

<th>ID</th>

<th>Employee</th>

<th>Department</th>

<th>Basic</th>

<th>Allowance</th>

<th>Deduction</th>

<th>Net Salary</th>

<th>Status</th>

</tr>

</thead>

<tbody id="payrollBody">

<tr>

<td>1</td>

<td>Dr. Kumar</td>

<td>Doctor</td>

<td>₹80,000</td>

<td>₹10,000</td>

<td>₹2,000</td>

<td>₹88,000</td>

<td><span class="salaryPaid">Paid</span></td>

</tr>

</tbody>

</table>

</section>

<style>

.payrollSection{

padding:90px 8%;

background:#f8fff7;

}

.payrollForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.payrollForm input,

.payrollForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.payrollForm button{

padding:15px;

background:#00897b;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.payrollCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.payrollCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.payrollCard h1{

font-size:42px;

color:#00897b;

}

.payrollTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.payrollTable th{

background:#00897b;

color:white;

padding:15px;

}

.payrollTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.salaryPaid{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

</style>

<script>

let payrollID=1;

function generateSalary(){

let employee=document.getElementById("salaryEmployee").value;

let department=document.getElementById("salaryDepartment").value;

let basic=parseFloat(document.getElementById("basicSalary").value);

let allowance=parseFloat(document.getElementById("allowance").value||0);

let deduction=parseFloat(document.getElementById("deduction").value||0);

if(employee==""||isNaN(basic)){

alert("Please fill all required fields");

return;

}

let netSalary=basic+allowance-deduction;

payrollID++;

let row="<tr>"+

"<td>"+payrollID+"</td>"+

"<td>"+employee+"</td>"+

"<td>"+department+"</td>"+

"<td>₹"+basic.toLocaleString()+"</td>"+

"<td>₹"+allowance.toLocaleString()+"</td>"+

"<td>₹"+deduction.toLocaleString()+"</td>"+

"<td>₹"+netSalary.toLocaleString()+"</td>"+

"<td><span class='salaryPaid'>Paid</span></td>"+

"</tr>";

document.getElementById("payrollBody").innerHTML+=row;

document.getElementById("employeesPaid").innerHTML=

parseInt(document.getElementById("employeesPaid").innerHTML)+1;

let total=parseInt(document.getElementById("totalPayroll").innerHTML.replace(/[₹,]/g,""));

document.getElementById("totalPayroll").innerHTML="₹"+(total+netSalary).toLocaleString("en-IN");

document.getElementById("salaryEmployee").value="";

document.getElementById("salaryID").value="";

document.getElementById("basicSalary").value="";

document.getElementById("allowance").value="";

document.getElementById("deduction").value="";

alert("💵 Salary generated successfully.");

}

</script>
<!-- ================= SUPPLIER & PURCHASE MANAGEMENT ================= -->

<section class="supplierSection">

<h2 class="title">🛒 Supplier & Purchase Management</h2>

<div class="supplierForm">

<input type="text" id="supplierName" placeholder="Supplier Name">

<input type="text" id="companyName" placeholder="Company Name">

<input type="text" id="purchaseItem" placeholder="Medicine / Equipment">

<input type="number" id="purchaseQty" placeholder="Quantity">

<input type="number" id="purchasePrice" placeholder="Unit Price (₹)">

<select id="purchaseStatus">

<option>Pending</option>
<option>Ordered</option>
<option>Delivered</option>

</select>

<button onclick="addPurchase()">

Create Purchase Order

</button>

</div>

<div class="supplierCards">

<div class="supplierCard">

<h1 id="totalSuppliers">65</h1>

<p>Total Suppliers</p>

</div>

<div class="supplierCard">

<h1 id="purchaseOrders">180</h1>

<p>Purchase Orders</p>

</div>

<div class="supplierCard">

<h1 id="pendingOrders">24</h1>

<p>Pending Orders</p>

</div>

<div class="supplierCard">

<h1 id="purchaseAmount">₹28,50,000</h1>

<p>Total Purchase</p>

</div>

</div>

<table class="supplierTable">

<thead>

<tr>

<th>ID</th>

<th>Supplier</th>

<th>Company</th>

<th>Item</th>

<th>Qty</th>

<th>Total</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="supplierBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>ABC Medicals</td>

<td>Paracetamol</td>

<td>1000</td>

<td>₹25,000</td>

<td><span class="orderedStatus">Ordered</span></td>

<td>

<button onclick="deliverOrder(this)">

Deliver

</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.supplierSection{

padding:90px 8%;

background:#fdfdf7;

}

.supplierForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.supplierForm input,

.supplierForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.supplierForm button{

padding:15px;

background:#ef6c00;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.supplierCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.supplierCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.supplierCard h1{

font-size:42px;

color:#ef6c00;

}

.supplierTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.supplierTable th{

background:#ef6c00;

color:white;

padding:15px;

}

.supplierTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.pendingStatus{

background:#ff9800;

color:white;

padding:6px 12px;

border-radius:20px;

}

.orderedStatus{

background:#1565c0;

color:white;

padding:6px 12px;

border-radius:20px;

}

.deliveredStatus{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.supplierTable button{

padding:8px 18px;

background:#ef6c00;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let purchaseID=1;

function addPurchase(){

let supplier=document.getElementById("supplierName").value;

let company=document.getElementById("companyName").value;

let item=document.getElementById("purchaseItem").value;

let qty=parseInt(document.getElementById("purchaseQty").value);

let price=parseFloat(document.getElementById("purchasePrice").value);

let status=document.getElementById("purchaseStatus").value;

if(supplier==""||company==""||item==""||isNaN(qty)||isNaN(price)){

alert("Please fill all fields");

return;

}

purchaseID++;

let total=qty*price;

let badge="<span class='pendingStatus'>Pending</span>";

if(status=="Ordered"){

badge="<span class='orderedStatus'>Ordered</span>";

}

if(status=="Delivered"){

badge="<span class='deliveredStatus'>Delivered</span>";

}

let row="<tr>"+

"<td>"+purchaseID+"</td>"+

"<td>"+supplier+"</td>"+

"<td>"+company+"</td>"+

"<td>"+item+"</td>"+

"<td>"+qty+"</td>"+

"<td>₹"+total.toLocaleString("en-IN")+"</td>"+

"<td>"+badge+"</td>"+

"<td><button onclick='deliverOrder(this)'>Deliver</button></td>"+

"</tr>";

document.getElementById("supplierBody").innerHTML+=row;

document.getElementById("purchaseOrders").innerHTML=

parseInt(document.getElementById("purchaseOrders").innerHTML)+1;

let amount=parseInt(document.getElementById("purchaseAmount").innerHTML.replace(/[₹,]/g,""));

document.getElementById("purchaseAmount").innerHTML="₹"+(amount+total).toLocaleString("en-IN");

document.getElementById("supplierName").value="";

document.getElementById("companyName").value="";

document.getElementById("purchaseItem").value="";

document.getElementById("purchaseQty").value="";

document.getElementById("purchasePrice").value="";

alert("🛒 Purchase Order Created Successfully");

}

function deliverOrder(btn){

let row=btn.parentElement.parentElement;

row.cells[6].innerHTML="<span class='deliveredStatus'>Delivered</span>";

btn.innerHTML="Delivered";

btn.disabled=true;

}

</script>
<!-- ================= PATIENT PORTAL ================= -->

<section class="patientPortalSection">

<h2 class="title">📱 Patient Portal</h2>

<div class="portalForm">

<input type="text" id="portalPatient" placeholder="Patient Name">

<input type="text" id="portalID" placeholder="Patient ID">

<input type="email" id="portalEmail" placeholder="Email">

<input type="tel" id="portalPhone" placeholder="Mobile Number">

<select id="portalGender">

<option>Male</option>
<option>Female</option>
<option>Other</option>

</select>

<button onclick="registerPortal()">

Create Patient Portal

</button>

</div>

<div class="portalCards">

<div class="portalCard">

<h1 id="portalUsers">820</h1>

<p>Portal Users</p>

</div>

<div class="portalCard">

<h1 id="onlineUsers">36</h1>

<p>Online Patients</p>

</div>

<div class="portalCard">

<h1 id="downloadsToday">54</h1>

<p>Reports Downloaded</p>

</div>

<div class="portalCard">

<h1 id="portalAppointments">112</h1>

<p>Appointments</p>

</div>

</div>

<table class="portalTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Patient ID</th>

<th>Email</th>

<th>Phone</th>

<th>Status</th>

<th>Actions</th>

</tr>

</thead>

<tbody id="portalBody">

<tr>

<td>1</td>

<td>Mohamed</td>

<td>P1001</td>

<td>mohamed@gmail.com</td>

<td>9876543210</td>

<td><span class="activePortal">Active</span></td>

<td>

<button onclick="viewPortal(this)">Profile</button>

<button onclick="downloadReport()">Reports</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.patientPortalSection{

padding:90px 8%;

background:#f4fcff;

}

.portalForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.portalForm input,

.portalForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.portalForm button{

padding:15px;

background:#1976d2;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.portalCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.portalCard{

background:white;

padding:30px;

border-radius:20px;

text-align:center;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.portalCard h1{

font-size:42px;

color:#1976d2;

}

.portalTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.portalTable th{

background:#1976d2;

color:white;

padding:15px;

}

.portalTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.activePortal{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.portalTable button{

padding:8px 14px;

margin:2px;

background:#1976d2;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let portalIDCounter=1;

function registerPortal(){

let patient=document.getElementById("portalPatient").value;

let pid=document.getElementById("portalID").value;

let email=document.getElementById("portalEmail").value;

let phone=document.getElementById("portalPhone").value;

if(patient==""||pid==""||email==""||phone==""){

alert("Please fill all fields");

return;

}

portalIDCounter++;

let row="<tr>"+

"<td>"+portalIDCounter+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+pid+"</td>"+

"<td>"+email+"</td>"+

"<td>"+phone+"</td>"+

"<td><span class='activePortal'>Active</span></td>"+

"<td><button onclick='viewPortal(this)'>Profile</button> <button onclick='downloadReport()'>Reports</button></td>"+

"</tr>";

document.getElementById("portalBody").innerHTML+=row;

document.getElementById("portalUsers").innerHTML=

parseInt(document.getElementById("portalUsers").innerHTML)+1;

document.getElementById("portalPatient").value="";

document.getElementById("portalID").value="";

document.getElementById("portalEmail").value="";

document.getElementById("portalPhone").value="";

alert("📱 Patient Portal Created Successfully");

}

function viewPortal(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+

"\nPatient ID : "+row.cells[2].innerHTML+

"\nEmail : "+row.cells[3].innerHTML+

"\nPhone : "+row.cells[4].innerHTML+

"\nStatus : "+row.cells[5].innerText

);

}

function downloadReport(){

alert("📄 Medical report downloaded successfully.");

}

</script>
<!-- ================= MULTI HOSPITAL BRANCH MANAGEMENT ================= -->

<section class="branchSection">

<h2 class="title">🏥 Multi-Hospital Branch Management</h2>

<div class="branchForm">

<input type="text" id="branchName" placeholder="Hospital Branch">

<input type="text" id="branchCity" placeholder="City">

<input type="text" id="branchManager" placeholder="Branch Manager">

<input type="number" id="branchDoctors" placeholder="Doctors">

<input type="number" id="branchBeds" placeholder="Beds">

<input type="number" id="branchRevenue" placeholder="Monthly Revenue (₹)">

<button onclick="addBranch()">

Add Branch

</button>

</div>

<div class="branchCards">

<div class="branchCard">

<h1 id="totalBranches">5</h1>

<p>Total Branches</p>

</div>

<div class="branchCard">

<h1 id="totalDoctorsBranch">210</h1>

<p>Total Doctors</p>

</div>

<div class="branchCard">

<h1 id="totalPatientsBranch">3850</h1>

<p>Total Patients</p>

</div>

<div class="branchCard">

<h1 id="networkRevenue">₹2,75,00,000</h1>

<p>Network Revenue</p>

</div>

</div>

<table class="branchTable">

<thead>

<tr>

<th>ID</th>

<th>Branch</th>

<th>City</th>

<th>Manager</th>

<th>Doctors</th>

<th>Beds</th>

<th>Revenue</th>

<th>Status</th>

</tr>

</thead>

<tbody id="branchBody">

<tr>

<td>1</td>

<td>City Hospital</td>

<td>Chennai</td>

<td>Mr. Kumar</td>

<td>45</td>

<td>180</td>

<td>₹45,00,000</td>

<td><span class="activeBranch">Active</span></td>

</tr>

</tbody>

</table>

</section>

<style>

.branchSection{

padding:90px 8%;

background:#f5fbff;

}

.branchForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.branchForm input{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.branchForm button{

padding:15px;

background:#0d47a1;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.branchCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.branchCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.branchCard h1{

font-size:42px;

color:#0d47a1;

}

.branchTable{

width:100%;

background:white;

border-collapse:collapse;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.branchTable th{

background:#0d47a1;

color:white;

padding:15px;

}

.branchTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.activeBranch{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.branchTable tr:hover{

background:#f0f8ff;

}

</style>

<script>

let branchID=1;

function addBranch(){

let name=document.getElementById("branchName").value;

let city=document.getElementById("branchCity").value;

let manager=document.getElementById("branchManager").value;

let doctors=parseInt(document.getElementById("branchDoctors").value);

let beds=parseInt(document.getElementById("branchBeds").value);

let revenue=parseFloat(document.getElementById("branchRevenue").value);

if(name==""||city==""||manager==""||isNaN(doctors)||isNaN(beds)||isNaN(revenue)){

alert("Please fill all fields");

return;

}

branchID++;

let row="<tr>"+

"<td>"+branchID+"</td>"+

"<td>"+name+"</td>"+

"<td>"+city+"</td>"+

"<td>"+manager+"</td>"+

"<td>"+doctors+"</td>"+

"<td>"+beds+"</td>"+

"<td>₹"+revenue.toLocaleString("en-IN")+"</td>"+

"<td><span class='activeBranch'>Active</span></td>"+

"</tr>";

document.getElementById("branchBody").innerHTML+=row;

document.getElementById("totalBranches").innerHTML=

parseInt(document.getElementById("totalBranches").innerHTML)+1;

document.getElementById("totalDoctorsBranch").innerHTML=

parseInt(document.getElementById("totalDoctorsBranch").innerHTML)+doctors;

let totalRevenue=parseInt(document.getElementById("networkRevenue").innerHTML.replace(/[₹,]/g,""));

document.getElementById("networkRevenue").innerHTML="₹"+(totalRevenue+revenue).toLocaleString("en-IN");

document.getElementById("branchName").value="";

document.getElementById("branchCity").value="";

document.getElementById("branchManager").value="";

document.getElementById("branchDoctors").value="";

document.getElementById("branchBeds").value="";

document.getElementById("branchRevenue").value="";

alert("🏥 Hospital Branch Added Successfully");

}

</script>
<!-- ================= SMS & EMAIL NOTIFICATION MANAGEMENT ================= -->

<section class="notificationSection">

<h2 class="title">🌐 SMS & Email Notification System</h2>

<div class="notificationForm">

<input type="text" id="notifyPatient" placeholder="Patient Name">

<input type="text" id="notifyContact" placeholder="Mobile Number / Email">

<select id="notifyType">

<option>Appointment Reminder</option>
<option>Medicine Reminder</option>
<option>Lab Report Ready</option>
<option>Bill Payment Reminder</option>
<option>Vaccination Reminder</option>
<option>Emergency Alert</option>
<option>General Announcement</option>

</select>

<textarea id="notifyMessage"
placeholder="Enter Notification Message"></textarea>

<button onclick="sendNotification()">

Send Notification

</button>

</div>

<div class="notifyCards">

<div class="notifyCard">

<h1 id="totalNotifications">3250</h1>

<p>Total Notifications</p>

</div>

<div class="notifyCard">

<h1 id="smsSent">1800</h1>

<p>SMS Sent</p>

</div>

<div class="notifyCard">

<h1 id="emailSent">1450</h1>

<p>Email Sent</p>

</div>

<div class="notifyCard">

<h1 id="deliveryRate">98%</h1>

<p>Delivery Rate</p>

</div>

</div>

<table class="notifyTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Contact</th>

<th>Type</th>

<th>Message</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="notifyBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>9876543210</td>

<td>Appointment Reminder</td>

<td>Your appointment is tomorrow at 10:00 AM.</td>

<td><span class="sentStatus">Sent</span></td>

<td>

<button onclick="viewNotification(this)">View</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.notificationSection{

padding:90px 8%;

background:#f5fcff;

}

.notificationForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(240px,1fr));

gap:15px;

margin-bottom:30px;

}

.notificationForm input,
.notificationForm select,
.notificationForm textarea{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

font-size:15px;

}

.notificationForm textarea{

min-height:120px;

resize:vertical;

}

.notificationForm button{

padding:15px;

background:#1565c0;

color:#fff;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.notifyCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.notifyCard{

background:#fff;

padding:25px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.notifyCard h1{

font-size:42px;

color:#1565c0;

}

.notifyTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.notifyTable th{

background:#1565c0;

color:white;

padding:15px;

}

.notifyTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.sentStatus{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.notifyTable button{

padding:8px 16px;

background:#1565c0;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let notificationID = 1;

function sendNotification(){

let patient=document.getElementById("notifyPatient").value;

let contact=document.getElementById("notifyContact").value;

let type=document.getElementById("notifyType").value;

let message=document.getElementById("notifyMessage").value;

if(patient=="" || contact=="" || message==""){

alert("Please fill all fields.");

return;

}

notificationID++;

let row="<tr>"+

"<td>"+notificationID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+contact+"</td>"+

"<td>"+type+"</td>"+

"<td>"+message+"</td>"+

"<td><span class='sentStatus'>Sent</span></td>"+

"<td><button onclick='viewNotification(this)'>View</button></td>"+

"</tr>";

document.getElementById("notifyBody").innerHTML+=row;

document.getElementById("totalNotifications").innerHTML=

parseInt(document.getElementById("totalNotifications").innerHTML)+1;

if(contact.includes("@")){

document.getElementById("emailSent").innerHTML=

parseInt(document.getElementById("emailSent").innerHTML)+1;

}else{

document.getElementById("smsSent").innerHTML=

parseInt(document.getElementById("smsSent").innerHTML)+1;

}

document.getElementById("notifyPatient").value="";

document.getElementById("notifyContact").value="";

document.getElementById("notifyMessage").value="";

alert("✅ Notification sent successfully.");

}

function viewNotification(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+

"\nContact : "+row.cells[2].innerHTML+

"\nType : "+row.cells[3].innerHTML+

"\nMessage : "+row.cells[4].innerHTML+

"\nStatus : "+row.cells[5].innerText

);

}

</script>
<!-- ================= ADVANCED INVENTORY MANAGEMENT ================= -->

<section class="inventorySection">

<h2 class="title">📦 Advanced Inventory & Stock Management</h2>

<div class="inventoryForm">

<input type="text" id="itemName" placeholder="Item Name">

<input type="text" id="itemCode" placeholder="Item Code">

<select id="itemCategory">

<option>Medicine</option>
<option>Surgical Equipment</option>
<option>Laboratory</option>
<option>Medical Consumables</option>
<option>Stationery</option>

</select>

<input type="text" id="batchNo" placeholder="Batch Number">

<input type="date" id="expiryDate">

<input type="number" id="stockQty" placeholder="Stock Quantity">

<input type="number" id="minimumStock" placeholder="Minimum Stock">

<button onclick="addInventory()">

Add Inventory

</button>

</div>

<div class="inventoryCards">

<div class="inventoryCard">

<h1 id="totalItems">850</h1>

<p>Total Items</p>

</div>

<div class="inventoryCard">

<h1 id="lowStockItems">14</h1>

<p>Low Stock</p>

</div>

<div class="inventoryCard">

<h1 id="expiringItems">8</h1>

<p>Expiring Soon</p>

</div>

<div class="inventoryCard">

<h1 id="inventoryValue">₹1,82,50,000</h1>

<p>Inventory Value</p>

</div>

</div>

<table class="inventoryTable">

<thead>

<tr>

<th>ID</th>

<th>Item</th>

<th>Code</th>

<th>Batch</th>

<th>Category</th>

<th>Expiry</th>

<th>Stock</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="inventoryBody">

<tr>

<td>1</td>

<td>Paracetamol 500mg</td>

<td>MED001</td>

<td>BT2401</td>

<td>Medicine</td>

<td>2027-05-20</td>

<td>550</td>

<td><span class="stockGood">Available</span></td>

<td>

<button onclick="reduceStock(this)">Issue</button>

<button onclick="restockItem(this)">Restock</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.inventorySection{

padding:90px 8%;

background:#f8fffb;

}

.inventoryForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.inventoryForm input,
.inventoryForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.inventoryForm button{

padding:15px;

background:#00897b;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.inventoryCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.inventoryCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 8px 18px rgba(0,0,0,.08);

}

.inventoryCard h1{

font-size:42px;

color:#00897b;

}

.inventoryTable{

width:100%;

background:white;

border-collapse:collapse;

border-radius:15px;

overflow:hidden;

box-shadow:0 8px 18px rgba(0,0,0,.08);

}

.inventoryTable th{

background:#00897b;

color:white;

padding:15px;

}

.inventoryTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.stockGood{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.stockLow{

background:#fb8c00;

color:white;

padding:6px 12px;

border-radius:20px;

}

.inventoryTable button{

padding:8px 14px;

margin:2px;

background:#00897b;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let inventoryID=1;

function addInventory(){

let item=document.getElementById("itemName").value;

let code=document.getElementById("itemCode").value;

let category=document.getElementById("itemCategory").value;

let batch=document.getElementById("batchNo").value;

let expiry=document.getElementById("expiryDate").value;

let qty=parseInt(document.getElementById("stockQty").value);

let minimum=parseInt(document.getElementById("minimumStock").value);

if(item==""||code==""||batch==""||expiry==""||isNaN(qty)||isNaN(minimum)){

alert("Please complete all fields.");

return;

}

inventoryID++;

let status="<span class='stockGood'>Available</span>";

if(qty<=minimum){

status="<span class='stockLow'>Low Stock</span>";

document.getElementById("lowStockItems").innerHTML=

parseInt(document.getElementById("lowStockItems").innerHTML)+1;

}

let row="<tr>"+

"<td>"+inventoryID+"</td>"+

"<td>"+item+"</td>"+

"<td>"+code+"</td>"+

"<td>"+batch+"</td>"+

"<td>"+category+"</td>"+

"<td>"+expiry+"</td>"+

"<td>"+qty+"</td>"+

"<td>"+status+"</td>"+

"<td><button onclick='reduceStock(this)'>Issue</button> <button onclick='restockItem(this)'>Restock</button></td>"+

"</tr>";

document.getElementById("inventoryBody").innerHTML+=row;

document.getElementById("totalItems").innerHTML=

parseInt(document.getElementById("totalItems").innerHTML)+1;

document.getElementById("itemName").value="";

document.getElementById("itemCode").value="";

document.getElementById("batchNo").value="";

document.getElementById("expiryDate").value="";

document.getElementById("stockQty").value="";

document.getElementById("minimumStock").value="";

alert("📦 Inventory added successfully.");

}

function reduceStock(btn){

let row=btn.parentElement.parentElement;

let qtyCell=row.cells[6];

let qty=parseInt(qtyCell.innerHTML);

if(qty>0){

qty--;

qtyCell.innerHTML=qty;

if(qty<=10){

row.cells[7].innerHTML="<span class='stockLow'>Low Stock</span>";

}

}

}

function restockItem(btn){

let row=btn.parentElement.parentElement;

let qtyCell=row.cells[6];

let qty=parseInt(qtyCell.innerHTML)+100;

qtyCell.innerHTML=qty;

row.cells[7].innerHTML="<span class='stockGood'>Available</span>";

alert("✅ Stock replenished successfully.");

}

</script>
<!-- ================= SECURITY & AUDIT LOG MANAGEMENT ================= -->

<section class="securitySection">

<h2 class="title">🔐 Security & Audit Log Management</h2>

<div class="securityForm">

<input type="text" id="userName" placeholder="Username">

<select id="userRole">

<option>Admin</option>
<option>Doctor</option>
<option>Nurse</option>
<option>Receptionist</option>
<option>Lab Technician</option>
<option>Pharmacist</option>

</select>

<input type="text" id="ipAddress" placeholder="IP Address">

<select id="loginStatus">

<option>Success</option>
<option>Failed</option>
<option>Password Changed</option>
<option>Account Locked</option>
<option>Logout</option>

</select>

<button onclick="addSecurityLog()">

Add Security Log

</button>

</div>

<div class="securityCards">

<div class="securityCard">

<h1 id="totalLogs">2458</h1>

<p>Total Logs</p>

</div>

<div class="securityCard">

<h1 id="successfulLogins">1980</h1>

<p>Successful Logins</p>

</div>

<div class="securityCard">

<h1 id="failedLogins">95</h1>

<p>Failed Logins</p>

</div>

<div class="securityCard">

<h1 id="lockedAccounts">6</h1>

<p>Locked Accounts</p>

</div>

</div>

<table class="securityTable">

<thead>

<tr>

<th>ID</th>

<th>User</th>

<th>Role</th>

<th>IP Address</th>

<th>Time</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="securityBody">

<tr>

<td>1</td>

<td>admin</td>

<td>Admin</td>

<td>192.168.1.10</td>

<td>09:30 AM</td>

<td><span class="successStatus">Success</span></td>

<td>

<button onclick="viewSecurityLog(this)">

View

</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.securitySection{

padding:90px 8%;

background:#fafbff;

}

.securityForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.securityForm input,

.securityForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.securityForm button{

padding:15px;

background:#5e35b1;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.securityCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.securityCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.securityCard h1{

font-size:42px;

color:#5e35b1;

}

.securityTable{

width:100%;

background:white;

border-collapse:collapse;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.securityTable th{

background:#5e35b1;

color:white;

padding:15px;

}

.securityTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.successStatus{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.failedStatus{

background:#d32f2f;

color:white;

padding:6px 12px;

border-radius:20px;

}

.lockedStatus{

background:#6d4c41;

color:white;

padding:6px 12px;

border-radius:20px;

}

.securityTable button{

padding:8px 16px;

background:#5e35b1;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let securityID=1;

function addSecurityLog(){

let user=document.getElementById("userName").value;

let role=document.getElementById("userRole").value;

let ip=document.getElementById("ipAddress").value;

let status=document.getElementById("loginStatus").value;

if(user==""||ip==""){

alert("Please fill all fields");

return;

}

securityID++;

let badge="<span class='successStatus'>"+status+"</span>";

if(status=="Failed"){

badge="<span class='failedStatus'>Failed</span>";

document.getElementById("failedLogins").innerHTML=

parseInt(document.getElementById("failedLogins").innerHTML)+1;

}

if(status=="Account Locked"){

badge="<span class='lockedStatus'>Locked</span>";

document.getElementById("lockedAccounts").innerHTML=

parseInt(document.getElementById("lockedAccounts").innerHTML)+1;

}

if(status=="Success"){

document.getElementById("successfulLogins").innerHTML=

parseInt(document.getElementById("successfulLogins").innerHTML)+1;

}

let time=new Date().toLocaleTimeString();

let row="<tr>"+

"<td>"+securityID+"</td>"+

"<td>"+user+"</td>"+

"<td>"+role+"</td>"+

"<td>"+ip+"</td>"+

"<td>"+time+"</td>"+

"<td>"+badge+"</td>"+

"<td><button onclick='viewSecurityLog(this)'>View</button></td>"+

"</tr>";

document.getElementById("securityBody").innerHTML+=row;

document.getElementById("totalLogs").innerHTML=

parseInt(document.getElementById("totalLogs").innerHTML)+1;

document.getElementById("userName").value="";

document.getElementById("ipAddress").value="";

alert("🔐 Security log added successfully.");

}

function viewSecurityLog(btn){

let row=btn.parentElement.parentElement;

alert(

"User : "+row.cells[1].innerHTML+

"\nRole : "+row.cells[2].innerHTML+

"\nIP : "+row.cells[3].innerHTML+

"\nTime : "+row.cells[4].innerHTML+

"\nStatus : "+row.cells[5].innerText

);

}

</script>
<!-- ================= ADVANCED REPORTS & ANALYTICS ================= -->

<section class="reportSection">

<h2 class="title">📊 Advanced Reports & Analytics</h2>

<div class="reportForm">

<select id="reportType">

<option>Revenue Report</option>
<option>Patient Report</option>
<option>Doctor Performance</option>
<option>Pharmacy Sales</option>
<option>Laboratory Report</option>
<option>Appointment Report</option>
<option>Insurance Report</option>

</select>

<input type="date" id="reportFrom">

<input type="date" id="reportTo">

<select id="reportFormat">

<option>PDF</option>
<option>Excel</option>
<option>CSV</option>

</select>

<button onclick="generateReport()">

Generate Report

</button>

</div>

<div class="reportCards">

<div class="reportCard">

<h1 id="reportsGenerated">540</h1>

<p>Reports Generated</p>

</div>

<div class="reportCard">

<h1 id="pdfReports">315</h1>

<p>PDF Reports</p>

</div>

<div class="reportCard">

<h1 id="excelReports">180</h1>

<p>Excel Reports</p>

</div>

<div class="reportCard">

<h1 id="csvReports">45</h1>

<p>CSV Reports</p>

</div>

</div>

<table class="reportTable">

<thead>

<tr>

<th>ID</th>

<th>Report Name</th>

<th>From</th>

<th>To</th>

<th>Format</th>

<th>Generated On</th>

<th>Status</th>

<th>Download</th>

</tr>

</thead>

<tbody id="reportBody">

<tr>

<td>1</td>

<td>Revenue Report</td>

<td>2026-07-01</td>

<td>2026-07-29</td>

<td>PDF</td>

<td>29-07-2026</td>

<td><span class="readyStatus">Ready</span></td>

<td>

<button onclick="downloadReport(this)">

Download

</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.reportSection{

padding:90px 8%;

background:#f8fbff;

}

.reportForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.reportForm input,

.reportForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.reportForm button{

padding:15px;

background:#3949ab;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.reportCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.reportCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 8px 20px rgba(0,0,0,.08);

}

.reportCard h1{

font-size:42px;

color:#3949ab;

}

.reportTable{

width:100%;

background:white;

border-collapse:collapse;

border-radius:15px;

overflow:hidden;

box-shadow:0 8px 20px rgba(0,0,0,.08);

}

.reportTable th{

background:#3949ab;

color:white;

padding:15px;

}

.reportTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.readyStatus{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.reportTable button{

padding:8px 16px;

background:#3949ab;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let reportID=1;

function generateReport(){

let type=document.getElementById("reportType").value;

let from=document.getElementById("reportFrom").value;

let to=document.getElementById("reportTo").value;

let format=document.getElementById("reportFormat").value;

if(from==""||to==""){

alert("Please select From and To dates.");

return;

}

reportID++;

let today=new Date().toLocaleDateString("en-GB");

let row="<tr>"+

"<td>"+reportID+"</td>"+

"<td>"+type+"</td>"+

"<td>"+from+"</td>"+

"<td>"+to+"</td>"+

"<td>"+format+"</td>"+

"<td>"+today+"</td>"+

"<td><span class='readyStatus'>Ready</span></td>"+

"<td><button onclick='downloadReport(this)'>Download</button></td>"+

"</tr>";

document.getElementById("reportBody").innerHTML+=row;

document.getElementById("reportsGenerated").innerHTML=

parseInt(document.getElementById("reportsGenerated").innerHTML)+1;

if(format=="PDF"){

document.getElementById("pdfReports").innerHTML=

parseInt(document.getElementById("pdfReports").innerHTML)+1;

}

if(format=="Excel"){

document.getElementById("excelReports").innerHTML=

parseInt(document.getElementById("excelReports").innerHTML)+1;

}

if(format=="CSV"){

document.getElementById("csvReports").innerHTML=

parseInt(document.getElementById("csvReports").innerHTML)+1;

}

alert("📊 Report generated successfully.");

}

function downloadReport(btn){

let row=btn.parentElement.parentElement;

alert("⬇ Downloading "+row.cells[1].innerHTML+" ("+row.cells[4].innerHTML+")");

}

</script>
<!-- ================= QR & BARCODE MANAGEMENT ================= -->

<section class="qrSection">

<h2 class="title">📷 QR Code & Barcode Management</h2>

<div class="qrForm">

<input type="text" id="qrPatient" placeholder="Patient / Medicine Name">

<input type="text" id="qrID" placeholder="Patient ID / Medicine Code">

<select id="qrType">

<option>Patient QR</option>
<option>Medicine Barcode</option>
<option>Lab Sample Barcode</option>
<option>Employee ID QR</option>
<option>Inventory QR</option>
<option>Billing QR</option>

</select>

<button onclick="generateQR()">

Generate Code

</button>

</div>

<div class="qrCards">

<div class="qrCard">

<h1 id="totalCodes">920</h1>

<p>Total Codes</p>

</div>

<div class="qrCard">

<h1 id="patientQR">380</h1>

<p>Patient QR</p>

</div>

<div class="qrCard">

<h1 id="medicineBarcode">420</h1>

<p>Medicine Barcode</p>

</div>

<div class="qrCard">

<h1 id="labBarcode">120</h1>

<p>Lab Barcodes</p>

</div>

</div>

<table class="qrTable">

<thead>

<tr>

<th>ID</th>

<th>Name</th>

<th>Reference ID</th>

<th>Type</th>

<th>Preview</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="qrBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>P1001</td>

<td>Patient QR</td>

<td><span style="font-size:28px;">⬛⬜⬛</span></td>

<td><span class="generatedStatus">Generated</span></td>

<td>

<button onclick="viewQR(this)">View</button>

<button onclick="printQR()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.qrSection{

padding:90px 8%;

background:#f9fcff;

}

.qrForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.qrForm input,

.qrForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.qrForm button{

padding:15px;

background:#00838f;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.qrCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.qrCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.qrCard h1{

font-size:42px;

color:#00838f;

}

.qrTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.qrTable th{

background:#00838f;

color:white;

padding:15px;

}

.qrTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.generatedStatus{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.qrTable button{

padding:8px 16px;

margin:2px;

background:#00838f;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let qrCodeID=1;

function generateQR(){

let name=document.getElementById("qrPatient").value;

let ref=document.getElementById("qrID").value;

let type=document.getElementById("qrType").value;

if(name==""||ref==""){

alert("Please fill all fields.");

return;

}

qrCodeID++;

let preview="⬛⬜⬛⬜⬛";

let row="<tr>"+

"<td>"+qrCodeID+"</td>"+

"<td>"+name+"</td>"+

"<td>"+ref+"</td>"+

"<td>"+type+"</td>"+

"<td style='font-size:26px;'>"+preview+"</td>"+

"<td><span class='generatedStatus'>Generated</span></td>"+

"<td><button onclick='viewQR(this)'>View</button> <button onclick='printQR()'>Print</button></td>"+

"</tr>";

document.getElementById("qrBody").innerHTML+=row;

document.getElementById("totalCodes").innerHTML=

parseInt(document.getElementById("totalCodes").innerHTML)+1;

if(type=="Patient QR"){

document.getElementById("patientQR").innerHTML=

parseInt(document.getElementById("patientQR").innerHTML)+1;

}

if(type=="Medicine Barcode"){

document.getElementById("medicineBarcode").innerHTML=

parseInt(document.getElementById("medicineBarcode").innerHTML)+1;

}

if(type=="Lab Sample Barcode"){

document.getElementById("labBarcode").innerHTML=

parseInt(document.getElementById("labBarcode").innerHTML)+1;

}

document.getElementById("qrPatient").value="";

document.getElementById("qrID").value="";

alert("📷 QR / Barcode generated successfully.");

}

function viewQR(btn){

let row=btn.parentElement.parentElement;

alert(

"Name : "+row.cells[1].innerHTML+

"\nReference ID : "+row.cells[2].innerHTML+

"\nType : "+row.cells[3].innerHTML+

"\nStatus : "+row.cells[5].innerText

);

}

function printQR(){

window.print();

}

</script>
<!-- ================= AI DISEASE PREDICTION SYSTEM ================= -->

<section class="aiDiseaseSection">

<h2 class="title">🤖 AI Disease Prediction System</h2>

<div class="aiForm">

<input type="text" id="patientNameAI" placeholder="Patient Name">

<input type="number" id="patientAgeAI" placeholder="Age">

<select id="patientGenderAI">

<option>Male</option>
<option>Female</option>
<option>Other</option>

</select>

<textarea id="patientSymptoms"
placeholder="Enter Symptoms (Example: Fever, Cough, Headache)"></textarea>

<button onclick="predictDisease()">

Predict Disease

</button>

</div>

<div class="aiCards">

<div class="aiCard">

<h1 id="predictionCount">1520</h1>

<p>Total Predictions</p>

</div>

<div class="aiCard">

<h1 id="highRiskCases">42</h1>

<p>High Risk Cases</p>

</div>

<div class="aiCard">

<h1 id="todayPrediction">18</h1>

<p>Today's Predictions</p>

</div>

<div class="aiCard">

<h1 id="accuracyAI">94%</h1>

<p>Model Accuracy</p>

</div>

</div>

<table class="predictionTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Symptoms</th>

<th>Predicted Disease</th>

<th>Risk</th>

<th>Doctor</th>

<th>Action</th>

</tr>

</thead>

<tbody id="predictionBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Fever, Cough</td>

<td>Viral Fever</td>

<td><span class="mediumRisk">Medium</span></td>

<td>General Physician</td>

<td>

<button onclick="viewPrediction(this)">View</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.aiDiseaseSection{

padding:90px 8%;

background:#f7fcff;

}

.aiForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(230px,1fr));

gap:15px;

margin-bottom:30px;

}

.aiForm input,

.aiForm select,

.aiForm textarea{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

font-size:15px;

}

.aiForm textarea{

min-height:120px;

resize:vertical;

}

.aiForm button{

padding:15px;

background:#6a1b9a;

color:#fff;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.aiCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.aiCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.aiCard h1{

font-size:42px;

color:#6a1b9a;

}

.predictionTable{

width:100%;

background:white;

border-collapse:collapse;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.predictionTable th{

background:#6a1b9a;

color:white;

padding:15px;

}

.predictionTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.lowRisk{

background:#43a047;

color:white;

padding:6px 12px;

border-radius:20px;

}

.mediumRisk{

background:#fb8c00;

color:white;

padding:6px 12px;

border-radius:20px;

}

.highRisk{

background:#d32f2f;

color:white;

padding:6px 12px;

border-radius:20px;

}

.predictionTable button{

padding:8px 16px;

background:#6a1b9a;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let predictionID=1;

function predictDisease(){

let patient=document.getElementById("patientNameAI").value;

let age=document.getElementById("patientAgeAI").value;

let symptoms=document.getElementById("patientSymptoms").value.toLowerCase();

if(patient==""||age==""||symptoms==""){

alert("Please fill all fields.");

return;

}

let disease="General Checkup";

let risk="Low";

let doctor="General Physician";

if(symptoms.includes("fever")&&symptoms.includes("cough")){

disease="Viral Fever";

risk="Medium";

}

if(symptoms.includes("chest pain")){

disease="Possible Heart Disease";

risk="High";

doctor="Cardiologist";

}

if(symptoms.includes("sugar")||symptoms.includes("frequent urination")){

disease="Possible Diabetes";

risk="Medium";

doctor="Diabetologist";

}

if(symptoms.includes("headache")&&symptoms.includes("blurred vision")){

disease="Migraine / Neurological Issue";

risk="Medium";

doctor="Neurologist";

}

let badge="<span class='lowRisk'>Low</span>";

if(risk=="Medium"){

badge="<span class='mediumRisk'>Medium</span>";

}

if(risk=="High"){

badge="<span class='highRisk'>High</span>";

document.getElementById("highRiskCases").innerHTML=

parseInt(document.getElementById("highRiskCases").innerHTML)+1;

}

predictionID++;

let row="<tr>"+

"<td>"+predictionID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+symptoms+"</td>"+

"<td>"+disease+"</td>"+

"<td>"+badge+"</td>"+

"<td>"+doctor+"</td>"+

"<td><button onclick='viewPrediction(this)'>View</button></td>"+

"</tr>";

document.getElementById("predictionBody").innerHTML+=row;

document.getElementById("predictionCount").innerHTML=

parseInt(document.getElementById("predictionCount").innerHTML)+1;

alert("🤖 AI Prediction Completed");

}

function viewPrediction(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+

"\nSymptoms : "+row.cells[2].innerHTML+

"\nPrediction : "+row.cells[3].innerHTML+

"\nRisk : "+row.cells[4].innerText+

"\nRecommended Doctor : "+row.cells[5].innerHTML+

"\n\n⚠ This prediction is for demonstration only and is NOT a medical diagnosis."

);

}

</script>
<!-- ================= AI MEDICINE RECOMMENDATION SYSTEM ================= -->

<section class="medicineAISection">

<h2 class="title">💊 AI Medicine Recommendation System</h2>

<div class="medicineForm">

<input type="text" id="medPatient" placeholder="Patient Name">

<input type="text" id="medDisease" placeholder="Predicted Disease">

<input type="text" id="medAllergy" placeholder="Known Allergy (Optional)">

<select id="medSeverity">

<option>Mild</option>
<option>Moderate</option>
<option>Severe</option>

</select>

<button onclick="recommendMedicine()">

Generate Recommendation

</button>

</div>

<div class="medicineCards">

<div class="medicineCard">

<h1 id="recommendationCount">860</h1>

<p>Total Recommendations</p>

</div>

<div class="medicineCard">

<h1 id="doctorApproval">645</h1>

<p>Approved</p>

</div>

<div class="medicineCard">

<h1 id="pendingApproval">215</h1>

<p>Pending Review</p>

</div>

<div class="medicineCard">

<h1 id="interactionAlerts">18</h1>

<p>Drug Alerts</p>

</div>

</div>

<table class="medicineTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Disease</th>

<th>Suggested Medicine</th>

<th>Dosage</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="medicineBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Viral Fever</td>

<td>Paracetamol*</td>

<td>500 mg - Every 6 hrs</td>

<td><span class="pendingBadge">Pending</span></td>

<td>

<button onclick="approveMedicine(this)">

Approve

</button>

</td>

</tr>

</tbody>

</table>

<p style="margin-top:20px;color:#c62828;font-weight:bold;">
* Educational demonstration only. Medication suggestions must always be reviewed and approved by a licensed healthcare professional.
</p>

</section>

<style>

.medicineAISection{

padding:90px 8%;

background:#fffdf7;

}

.medicineForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.medicineForm input,

.medicineForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.medicineForm button{

padding:15px;

background:#00897b;

color:white;

border:none;

border-radius:10px;

cursor:pointer;

font-weight:bold;

}

.medicineCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.medicineCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.medicineCard h1{

font-size:42px;

color:#00897b;

}

.medicineTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.medicineTable th{

background:#00897b;

color:white;

padding:15px;

}

.medicineTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.pendingBadge{

background:#fb8c00;

color:white;

padding:6px 12px;

border-radius:20px;

}

.approvedBadge{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.medicineTable button{

padding:8px 16px;

background:#00897b;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let medicineID=1;

function recommendMedicine(){

let patient=document.getElementById("medPatient").value;

let disease=document.getElementById("medDisease").value.toLowerCase();

let allergy=document.getElementById("medAllergy").value.toLowerCase();

let severity=document.getElementById("medSeverity").value;

if(patient=="" || disease==""){

alert("Please fill all required fields.");

return;

}

let medicine="Consult Physician";

let dosage="Doctor Decision";

if(disease.includes("viral")){

medicine="Paracetamol*";

dosage="500 mg - Every 6 hrs";

}

else if(disease.includes("diabetes")){

medicine="Metformin*";

dosage="500 mg - Twice Daily";

}

else if(disease.includes("heart")){

medicine="Cardiology Evaluation Required";

dosage="Specialist Decision";

}

else if(disease.includes("migraine")){

medicine="Pain Relief (Doctor Review)*";

dosage="As Prescribed";

}

if(allergy.includes("paracetamol") && medicine.includes("Paracetamol")){

alert("⚠ Allergy warning: Patient reports Paracetamol allergy.");

document.getElementById("interactionAlerts").innerHTML=

parseInt(document.getElementById("interactionAlerts").innerHTML)+1;

}

medicineID++;

let row="<tr>"+

"<td>"+medicineID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+disease+"</td>"+

"<td>"+medicine+"</td>"+

"<td>"+dosage+"</td>"+

"<td><span class='pendingBadge'>Pending</span></td>"+

"<td><button onclick='approveMedicine(this)'>Approve</button></td>"+

"</tr>";

document.getElementById("medicineBody").innerHTML+=row;

document.getElementById("recommendationCount").innerHTML=

parseInt(document.getElementById("recommendationCount").innerHTML)+1;

}

function approveMedicine(btn){

let row=btn.parentElement.parentElement;

row.cells[5].innerHTML="<span class='approvedBadge'>Approved</span>";

btn.innerHTML="Approved";

btn.disabled=true;

document.getElementById("doctorApproval").innerHTML=

parseInt(document.getElementById("doctorApproval").innerHTML)+1;

document.getElementById("pendingApproval").innerHTML=

parseInt(document.getElementById("pendingApproval").innerHTML)-1;

alert("👨‍⚕️ Recommendation approved by doctor.");

}

</script>
<!-- ================= AI VOICE ASSISTANT ================= -->

<section class="voiceSection">

<h2 class="title">🎤 AI Voice Assistant</h2>

<div class="voiceForm">

<input type="text" id="voicePatient" placeholder="Patient Name">

<select id="voiceCommand">

<option>Book Appointment</option>
<option>Patient Registration</option>
<option>Check Appointment</option>
<option>Find Doctor</option>
<option>Medicine Reminder</option>
<option>Hospital Navigation</option>
<option>Emergency Call</option>

</select>

<button onclick="startVoiceRecognition()">

🎙️ Start Voice

</button>

<button onclick="executeVoiceCommand()">

🤖 Execute Command

</button>

</div>

<div class="voiceCards">

<div class="voiceCard">

<h1 id="voiceCommands">1240</h1>

<p>Total Commands</p>

</div>

<div class="voiceCard">

<h1 id="successfulVoice">1185</h1>

<p>Successful</p>

</div>

<div class="voiceCard">

<h1 id="voiceLanguages">12</h1>

<p>Languages</p>

</div>

<div class="voiceCard">

<h1 id="activeVoiceUsers">28</h1>

<p>Active Users</p>

</div>

</div>

<table class="voiceTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Command</th>

<th>Recognized Text</th>

<th>Status</th>

<th>Time</th>

<th>Action</th>

</tr>

</thead>

<tbody id="voiceBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Book Appointment</td>

<td>"Book my appointment tomorrow"</td>

<td><span class="voiceSuccess">Completed</span></td>

<td>10:45 AM</td>

<td>

<button onclick="playResponse()">

🔊 Play

</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.voiceSection{

padding:90px 8%;

background:#f8fbff;

}

.voiceForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.voiceForm input,

.voiceForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.voiceForm button{

padding:15px;

background:#673ab7;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.voiceCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.voiceCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.voiceCard h1{

font-size:42px;

color:#673ab7;

}

.voiceTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.voiceTable th{

background:#673ab7;

color:white;

padding:15px;

}

.voiceTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.voiceSuccess{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.voiceTable button{

padding:8px 15px;

background:#673ab7;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let voiceID=1;

function startVoiceRecognition(){

if(!('webkitSpeechRecognition' in window)){

alert("Speech Recognition is not supported in this browser.");

return;

}

const recognition=new webkitSpeechRecognition();

recognition.lang="en-IN";

recognition.start();

recognition.onresult=function(event){

let transcript=event.results[0][0].transcript;

document.getElementById("voicePatient").value=transcript;

alert("🎤 Voice Recognized: "+transcript);

};

}

function executeVoiceCommand(){

let patient=document.getElementById("voicePatient").value;

let command=document.getElementById("voiceCommand").value;

if(patient==""){

alert("Please speak or enter patient name.");

return;

}

voiceID++;

let time=new Date().toLocaleTimeString();

let row="<tr>"+

"<td>"+voiceID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+command+"</td>"+

"<td>\""+patient+"\"</td>"+

"<td><span class='voiceSuccess'>Completed</span></td>"+

"<td>"+time+"</td>"+

"<td><button onclick='playResponse()'>🔊 Play</button></td>"+

"</tr>";

document.getElementById("voiceBody").innerHTML+=row;

document.getElementById("voiceCommands").innerHTML=

parseInt(document.getElementById("voiceCommands").innerHTML)+1;

document.getElementById("successfulVoice").innerHTML=

parseInt(document.getElementById("successfulVoice").innerHTML)+1;

alert("✅ Voice command executed successfully.");

}

function playResponse(){

const msg=new SpeechSynthesisUtterance(

"Your request has been completed successfully."

);

msg.lang="en-IN";

window.speechSynthesis.speak(msg);

}

</script>
<!-- ================= CLOUD BACKUP & DISASTER RECOVERY ================= -->

<section class="backupSection">

<h2 class="title">☁️ Cloud Backup & Disaster Recovery</h2>

<div class="backupForm">

<select id="backupType">

<option>Full Database Backup</option>
<option>Patient Records</option>
<option>Billing Data</option>
<option>Laboratory Data</option>
<option>Medical Images</option>
<option>Entire Hospital System</option>

</select>

<select id="backupStorage">

<option>Google Cloud</option>
<option>AWS S3</option>
<option>Microsoft Azure</option>
<option>Private Cloud</option>

</select>

<select id="backupEncryption">

<option>AES-256 Encryption</option>
<option>AES-128 Encryption</option>

</select>

<button onclick="startBackup()">

Start Backup

</button>

<button onclick="restoreBackup()">

Restore Backup

</button>

</div>

<div class="backupCards">

<div class="backupCard">

<h1 id="totalBackups">580</h1>

<p>Total Backups</p>

</div>

<div class="backupCard">

<h1 id="successfulBackups">565</h1>

<p>Successful</p>

</div>

<div class="backupCard">

<h1 id="restoreCount">25</h1>

<p>Restores</p>

</div>

<div class="backupCard">

<h1 id="backupStorageUsed">1.8 TB</h1>

<p>Storage Used</p>

</div>

</div>

<table class="backupTable">

<thead>

<tr>

<th>ID</th>

<th>Backup Type</th>

<th>Cloud</th>

<th>Encryption</th>

<th>Date & Time</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="backupBody">

<tr>

<td>1</td>

<td>Full Database Backup</td>

<td>AWS S3</td>

<td>AES-256</td>

<td>29-07-2026 10:30 AM</td>

<td><span class="backupSuccess">Completed</span></td>

<td>

<button onclick="downloadBackup(this)">Download</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.backupSection{

padding:90px 8%;

background:#f6fbff;

}

.backupForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.backupForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.backupForm button{

padding:15px;

background:#0277bd;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.backupCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.backupCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.backupCard h1{

font-size:42px;

color:#0277bd;

}

.backupTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.backupTable th{

background:#0277bd;

color:white;

padding:15px;

}

.backupTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.backupSuccess{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.backupTable button{

padding:8px 16px;

background:#0277bd;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let backupID=1;

function startBackup(){

let type=document.getElementById("backupType").value;

let cloud=document.getElementById("backupStorage").value;

let encryption=document.getElementById("backupEncryption").value;

backupID++;

let now=new Date().toLocaleString();

let row="<tr>"+

"<td>"+backupID+"</td>"+

"<td>"+type+"</td>"+

"<td>"+cloud+"</td>"+

"<td>"+encryption+"</td>"+

"<td>"+now+"</td>"+

"<td><span class='backupSuccess'>Completed</span></td>"+

"<td><button onclick='downloadBackup(this)'>Download</button></td>"+

"</tr>";

document.getElementById("backupBody").innerHTML+=row;

document.getElementById("totalBackups").innerHTML=

parseInt(document.getElementById("totalBackups").innerHTML)+1;

document.getElementById("successfulBackups").innerHTML=

parseInt(document.getElementById("successfulBackups").innerHTML)+1;

alert("☁️ Backup completed successfully.");

}

function restoreBackup(){

document.getElementById("restoreCount").innerHTML=

parseInt(document.getElementById("restoreCount").innerHTML)+1;

alert("🔄 Backup restored successfully.");

}

function downloadBackup(btn){

let row=btn.parentElement.parentElement;

alert("⬇ Downloading "+row.cells[1].innerHTML);

}

</script><!-- ================= AI MEDICAL IMAGE ANALYSIS ================= -->

<section class="imageAISection">

<h2 class="title">🧠 AI Medical Image Analysis</h2>

<div class="imageForm">

<input type="text" id="scanPatient" placeholder="Patient Name">

<input type="text" id="scanID" placeholder="Patient ID">

<select id="scanType">

<option>X-Ray</option>
<option>CT Scan</option>
<option>MRI</option>
<option>Ultrasound</option>
<option>ECG</option>

</select>

<input type="file" id="scanImage" accept="image/*">

<button onclick="analyzeImage()">

Analyze Scan

</button>

</div>

<div class="imageCards">

<div class="imageCard">

<h1 id="totalScans">820</h1>

<p>Total Scans</p>

</div>

<div class="imageCard">

<h1 id="normalScans">605</h1>

<p>Normal</p>

</div>

<div class="imageCard">

<h1 id="abnormalScans">215</h1>

<p>Abnormal</p>

</div>

<div class="imageCard">

<h1 id="analysisAccuracy">96%</h1>

<p>AI Accuracy</p>

</div>

</div>

<table class="scanTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Scan</th>

<th>AI Result</th>

<th>Confidence</th>

<th>Radiologist</th>

<th>Action</th>

</tr>

</thead>

<tbody id="scanBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Chest X-Ray</td>

<td>Normal</td>

<td>98%</td>

<td>Pending Review</td>

<td>

<button onclick="viewScan(this)">View</button>

<button onclick="approveScan(this)">Approve</button>

</td>

</tr>

</tbody>

</table>

<p style="margin-top:20px;color:#d32f2f;font-weight:bold;">
⚠ AI analysis is an assistive tool only. Final diagnosis must always be confirmed by a qualified radiologist or physician.
</p>

</section>

<style>

.imageAISection{
padding:90px 8%;
background:#f8fbff;
}

.imageForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.imageForm input,
.imageForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.imageForm button{
padding:15px;
background:#1565c0;
color:white;
border:none;
border-radius:10px;
cursor:pointer;
font-weight:bold;
}

.imageCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.imageCard{
background:white;
padding:30px;
text-align:center;
border-radius:20px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.imageCard h1{
font-size:42px;
color:#1565c0;
}

.scanTable{
width:100%;
background:white;
border-collapse:collapse;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.scanTable th{
background:#1565c0;
color:white;
padding:15px;
}

.scanTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.normalScan{
background:#2e7d32;
color:white;
padding:6px 12px;
border-radius:20px;
}

.abnormalScan{
background:#d32f2f;
color:white;
padding:6px 12px;
border-radius:20px;
}

.scanTable button{
padding:8px 15px;
margin:2px;
background:#1565c0;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let scanIDCounter=1;

function analyzeImage(){

let patient=document.getElementById("scanPatient").value;
let scan=document.getElementById("scanType").value;

if(patient==""){

alert("Please enter patient name.");

return;

}

scanIDCounter++;

let abnormal=Math.random()<0.3;

let result=abnormal?
"<span class='abnormalScan'>Abnormal</span>":
"<span class='normalScan'>Normal</span>";

let confidence=Math.floor(Math.random()*8)+92;

if(abnormal){

document.getElementById("abnormalScans").innerHTML=
parseInt(document.getElementById("abnormalScans").innerHTML)+1;

}else{

document.getElementById("normalScans").innerHTML=
parseInt(document.getElementById("normalScans").innerHTML)+1;

}

let row="<tr>"+
"<td>"+scanIDCounter+"</td>"+
"<td>"+patient+"</td>"+
"<td>"+scan+"</td>"+
"<td>"+result+"</td>"+
"<td>"+confidence+"%</td>"+
"<td>Pending Review</td>"+
"<td><button onclick='viewScan(this)'>View</button> <button onclick='approveScan(this)'>Approve</button></td>"+
"</tr>";

document.getElementById("scanBody").innerHTML+=row;

document.getElementById("totalScans").innerHTML=
parseInt(document.getElementById("totalScans").innerHTML)+1;

alert("🧠 AI image analysis completed.");

}

function approveScan(btn){

let row=btn.parentElement.parentElement;

row.cells[5].innerHTML="Approved";

btn.innerHTML="Approved";

btn.disabled=true;

alert("✅ Report approved by Radiologist.");

}

function viewScan(btn){

let row=btn.parentElement.parentElement;

alert(
"Patient : "+row.cells[1].innerHTML+
"\nScan : "+row.cells[2].innerHTML+
"\nAI Result : "+row.cells[3].innerText+
"\nConfidence : "+row.cells[4].innerHTML+
"\nReviewer : "+row.cells[5].innerHTML+
"\n\n⚠ AI output is for assistance only and is not a final diagnosis."
);

}

</script>
<!-- ================= FACE RECOGNITION SYSTEM ================= -->

<section class="faceSection">

<h2 class="title">👤 Face Recognition Attendance & Patient Check-in</h2>

<div class="faceForm">

<input type="text" id="faceName" placeholder="Patient / Employee Name">

<input type="text" id="faceID" placeholder="Patient ID / Employee ID">

<select id="faceRole">

<option>Patient</option>
<option>Doctor</option>
<option>Nurse</option>
<option>Receptionist</option>
<option>Staff</option>
<option>Visitor</option>

</select>

<input type="file" id="faceImage" accept="image/*">

<button onclick="captureFace()">

📷 Capture Face

</button>

<button onclick="verifyFace()">

😀 Verify Identity

</button>

</div>

<div class="faceCards">

<div class="faceCard">

<h1 id="registeredFaces">1520</h1>

<p>Registered Faces</p>

</div>

<div class="faceCard">

<h1 id="todayCheckins">318</h1>

<p>Today's Check-ins</p>

</div>

<div class="faceCard">

<h1 id="attendanceMarked">246</h1>

<p>Attendance Marked</p>

</div>

<div class="faceCard">

<h1 id="recognitionAccuracy">98%</h1>

<p>Recognition Accuracy</p>

</div>

</div>

<table class="faceTable">

<thead>

<tr>

<th>ID</th>

<th>Name</th>

<th>Role</th>

<th>Check-in Time</th>

<th>Status</th>

<th>Verification</th>

<th>Action</th>

</tr>

</thead>

<tbody id="faceBody">

<tr>

<td>1</td>

<td>Dr. Kumar</td>

<td>Doctor</td>

<td>09:00 AM</td>

<td><span class="verifiedFace">Present</span></td>

<td>Verified</td>

<td>

<button onclick="viewFace(this)">View</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.faceSection{

padding:90px 8%;

background:#f8fcff;

}

.faceForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.faceForm input,

.faceForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.faceForm button{

padding:15px;

background:#00796b;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.faceCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.faceCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.faceCard h1{

font-size:42px;

color:#00796b;

}

.faceTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.faceTable th{

background:#00796b;

color:white;

padding:15px;

}

.faceTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.verifiedFace{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.failedFace{

background:#d32f2f;

color:white;

padding:6px 12px;

border-radius:20px;

}

.faceTable button{

padding:8px 16px;

background:#00796b;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let faceIDCounter=1;

function captureFace(){

alert("📷 Face image captured successfully (Demo).");

}

function verifyFace(){

let name=document.getElementById("faceName").value;

let role=document.getElementById("faceRole").value;

if(name==""){

alert("Please enter a name.");

return;

}

faceIDCounter++;

let verified=Math.random()>0.1;

let status=verified?
"<span class='verifiedFace'>Verified</span>":
"<span class='failedFace'>Failed</span>";

let attendance=verified?"Present":"Rejected";

if(verified){

document.getElementById("todayCheckins").innerHTML=

parseInt(document.getElementById("todayCheckins").innerHTML)+1;

document.getElementById("attendanceMarked").innerHTML=

parseInt(document.getElementById("attendanceMarked").innerHTML)+1;

}

let time=new Date().toLocaleTimeString();

let row="<tr>"+

"<td>"+faceIDCounter+"</td>"+

"<td>"+name+"</td>"+

"<td>"+role+"</td>"+

"<td>"+time+"</td>"+

"<td>"+status+"</td>"+

"<td>"+attendance+"</td>"+

"<td><button onclick='viewFace(this)'>View</button></td>"+

"</tr>";

document.getElementById("faceBody").innerHTML+=row;

alert(verified?
"✅ Identity verified successfully.":
"❌ Face verification failed.");

}

function viewFace(btn){

let row=btn.parentElement.parentElement;

alert(

"Name : "+row.cells[1].innerHTML+

"\nRole : "+row.cells[2].innerHTML+

"\nCheck-in : "+row.cells[3].innerHTML+

"\nStatus : "+row.cells[4].innerText+

"\nAttendance : "+row.cells[5].innerHTML

);

}

</script>
<!-- ================= SUPER ADMIN & MULTI TENANT ================= -->

<section class="superAdminSection">

<h2 class="title">🏢 Super Admin & SaaS Multi-Tenant Management</h2>

<div class="tenantForm">

<input type="text" id="hospitalName" placeholder="Hospital Name">

<input type="text" id="tenantCode" placeholder="Tenant Code">

<input type="text" id="adminName" placeholder="Admin Name">

<input type="email" id="adminEmail" placeholder="Admin Email">

<select id="tenantPlan">

<option>Free</option>
<option>Basic</option>
<option>Professional</option>
<option>Enterprise</option>

</select>

<select id="tenantStatus">

<option>Active</option>
<option>Trial</option>
<option>Suspended</option>
<option>Expired</option>

</select>

<button onclick="addTenant()">

Create Hospital

</button>

</div>

<div class="tenantCards">

<div class="tenantCard">

<h1 id="totalHospitals">45</h1>

<p>Total Hospitals</p>

</div>

<div class="tenantCard">

<h1 id="activeHospitals">38</h1>

<p>Active</p>

</div>

<div class="tenantCard">

<h1 id="trialHospitals">5</h1>

<p>Trial</p>

</div>

<div class="tenantCard">

<h1 id="monthlyRevenue">₹18,75,000</h1>

<p>Monthly Revenue</p>

</div>

</div>

<table class="tenantTable">

<thead>

<tr>

<th>ID</th>

<th>Hospital</th>

<th>Tenant Code</th>

<th>Plan</th>

<th>Admin</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="tenantBody">

<tr>

<td>1</td>

<td>ABC Hospital</td>

<td>HSP001</td>

<td>Enterprise</td>

<td>Dr. Kumar</td>

<td><span class="activeTenant">Active</span></td>

<td>

<button onclick="manageTenant(this)">Manage</button>

<button onclick="disableTenant(this)">Disable</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.superAdminSection{

padding:90px 8%;

background:#f8f9ff;

}

.tenantForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.tenantForm input,

.tenantForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.tenantForm button{

padding:15px;

background:#512da8;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.tenantCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.tenantCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.tenantCard h1{

font-size:42px;

color:#512da8;

}

.tenantTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.tenantTable th{

background:#512da8;

color:white;

padding:15px;

}

.tenantTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.activeTenant{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.trialTenant{

background:#fb8c00;

color:white;

padding:6px 12px;

border-radius:20px;

}

.suspendedTenant{

background:#d32f2f;

color:white;

padding:6px 12px;

border-radius:20px;

}

.tenantTable button{

padding:8px 14px;

margin:2px;

background:#512da8;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let tenantID=1;

function addTenant(){

let hospital=document.getElementById("hospitalName").value;

let code=document.getElementById("tenantCode").value;

let admin=document.getElementById("adminName").value;

let plan=document.getElementById("tenantPlan").value;

let status=document.getElementById("tenantStatus").value;

if(hospital==""||code==""||admin==""){

alert("Please fill all required fields.");

return;

}

tenantID++;

let badge="<span class='activeTenant'>Active</span>";

if(status=="Trial"){

badge="<span class='trialTenant'>Trial</span>";

document.getElementById("trialHospitals").innerHTML=

parseInt(document.getElementById("trialHospitals").innerHTML)+1;

}

if(status=="Suspended"||status=="Expired"){

badge="<span class='suspendedTenant'>"+status+"</span>";

}

if(status=="Active"){

document.getElementById("activeHospitals").innerHTML=

parseInt(document.getElementById("activeHospitals").innerHTML)+1;

}

let row="<tr>"+

"<td>"+(++tenantID)+"</td>"+

"<td>"+hospital+"</td>"+

"<td>"+code+"</td>"+

"<td>"+plan+"</td>"+

"<td>"+admin+"</td>"+

"<td>"+badge+"</td>"+

"<td><button onclick='manageTenant(this)'>Manage</button> <button onclick='disableTenant(this)'>Disable</button></td>"+

"</tr>";

document.getElementById("tenantBody").innerHTML+=row;

document.getElementById("totalHospitals").innerHTML=

parseInt(document.getElementById("totalHospitals").innerHTML)+1;

alert("🏥 Hospital tenant created successfully.");

}

function manageTenant(btn){

let row=btn.parentElement.parentElement;

alert(

"Hospital : "+row.cells[1].innerHTML+

"\nTenant : "+row.cells[2].innerHTML+

"\nPlan : "+row.cells[3].innerHTML+

"\nAdmin : "+row.cells[4].innerHTML

);

}

function disableTenant(btn){

let row=btn.parentElement.parentElement;

row.cells[5].innerHTML="<span class='suspendedTenant'>Suspended</span>";

alert("🚫 Hospital access suspended.");

}

</script>
<!-- ================= IOT PATIENT MONITORING ================= -->

<section class="iotSection">

<h2 class="title">📡 IoT Patient Monitoring</h2>

<div class="iotForm">

<input type="text" id="iotPatient" placeholder="Patient Name">

<input type="text" id="iotBed" placeholder="Bed Number">

<select id="iotWard">

<option>ICU</option>
<option>CCU</option>
<option>NICU</option>
<option>General Ward</option>
<option>Emergency</option>

</select>

<select id="iotDevice">

<option>Heart Rate Monitor</option>
<option>Blood Pressure Monitor</option>
<option>SpO₂ Sensor</option>
<option>Temperature Sensor</option>
<option>ECG Monitor</option>

</select>

<button onclick="connectDevice()">

📶 Connect Device

</button>

</div>

<div class="iotCards">

<div class="iotCard">

<h1 id="connectedDevices">186</h1>

<p>Connected Devices</p>

</div>

<div class="iotCard">

<h1 id="activePatients">142</h1>

<p>Active Patients</p>

</div>

<div class="iotCard">

<h1 id="criticalAlerts">8</h1>

<p>Critical Alerts</p>

</div>

<div class="iotCard">

<h1 id="avgHeartRate">78</h1>

<p>Average Heart Rate</p>

</div>

</div>

<table class="iotTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Device</th>

<th>Heart Rate</th>

<th>SpO₂</th>

<th>Temperature</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="iotBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>ECG Monitor</td>

<td>76 bpm</td>

<td>98%</td>

<td>36.8°C</td>

<td><span class="iotNormal">Normal</span></td>

<td>

<button onclick="viewVitals(this)">View</button>

<button onclick="sendAlert(this)">Alert</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.iotSection{
padding:90px 8%;
background:#f6fcff;
}

.iotForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.iotForm input,
.iotForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.iotForm button{
padding:15px;
background:#009688;
color:white;
border:none;
border-radius:10px;
cursor:pointer;
font-weight:bold;
}

.iotCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.iotCard{
background:white;
padding:30px;
text-align:center;
border-radius:20px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.iotCard h1{
font-size:42px;
color:#009688;
}

.iotTable{
width:100%;
border-collapse:collapse;
background:white;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.iotTable th{
background:#009688;
color:white;
padding:15px;
}

.iotTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.iotNormal{
background:#2e7d32;
color:white;
padding:6px 12px;
border-radius:20px;
}

.iotCritical{
background:#d32f2f;
color:white;
padding:6px 12px;
border-radius:20px;
}

.iotTable button{
padding:8px 14px;
margin:2px;
background:#009688;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let monitorID=1;

function connectDevice(){

let patient=document.getElementById("iotPatient").value;

let device=document.getElementById("iotDevice").value;

if(patient==""){

alert("Enter patient name.");

return;

}

monitorID++;

let heart=Math.floor(Math.random()*40)+60;

let spo2=Math.floor(Math.random()*6)+94;

let temp=(36+Math.random()*2).toFixed(1);

let critical=(heart>110||spo2<95||temp>38);

let status=critical?
"<span class='iotCritical'>Critical</span>":
"<span class='iotNormal'>Normal</span>";

if(critical){

document.getElementById("criticalAlerts").innerHTML=

parseInt(document.getElementById("criticalAlerts").innerHTML)+1;

}

let row="<tr>"+

"<td>"+monitorID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+device+"</td>"+

"<td>"+heart+" bpm</td>"+

"<td>"+spo2+"%</td>"+

"<td>"+temp+"°C</td>"+

"<td>"+status+"</td>"+

"<td><button onclick='viewVitals(this)'>View</button> <button onclick='sendAlert(this)'>Alert</button></td>"+

"</tr>";

document.getElementById("iotBody").innerHTML+=row;

document.getElementById("connectedDevices").innerHTML=

parseInt(document.getElementById("connectedDevices").innerHTML)+1;

document.getElementById("activePatients").innerHTML=

parseInt(document.getElementById("activePatients").innerHTML)+1;

alert("📡 IoT device connected successfully.");

}

function viewVitals(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+

"\nDevice : "+row.cells[2].innerHTML+

"\nHeart Rate : "+row.cells[3].innerHTML+

"\nSpO₂ : "+row.cells[4].innerHTML+

"\nTemperature : "+row.cells[5].innerHTML+

"\nStatus : "+row.cells[6].innerText

);

}

function sendAlert(btn){

alert("🚨 Critical alert sent to Doctor, ICU Dashboard and Nurse Station.");

}

</script>
<!-- ================= MOBILE API & PUSH NOTIFICATIONS ================= -->

<section class="mobileSection">

<h2 class="title">📱 Mobile App API & Push Notification</h2>

<div class="mobileForm">

<input type="text" id="mobilePatient" placeholder="Patient Name">

<input type="text" id="deviceToken" placeholder="Device Token">

<select id="notificationType">

<option>Appointment Reminder</option>
<option>Medicine Reminder</option>
<option>Lab Report Ready</option>
<option>Bill Payment Due</option>
<option>Emergency Alert</option>
<option>Doctor Message</option>

</select>

<select id="platform">

<option>Android</option>
<option>iOS</option>
<option>Web App</option>

</select>

<button onclick="sendPushNotification()">

📲 Send Notification

</button>

</div>

<div class="mobileCards">

<div class="mobileCard">

<h1 id="totalNotifications">15840</h1>

<p>Total Notifications</p>

</div>

<div class="mobileCard">

<h1 id="successfulNotifications">15498</h1>

<p>Delivered</p>

</div>

<div class="mobileCard">

<h1 id="activeDevices">4521</h1>

<p>Active Devices</p>

</div>

<div class="mobileCard">

<h1 id="apiRequests">128450</h1>

<p>API Requests Today</p>

</div>

</div>

<table class="mobileTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Platform</th>

<th>Notification</th>

<th>Status</th>

<th>Time</th>

<th>Action</th>

</tr>

</thead>

<tbody id="mobileBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Android</td>

<td>Appointment Reminder</td>

<td><span class="mobileSuccess">Delivered</span></td>

<td>10:20 AM</td>

<td>

<button onclick="viewNotification(this)">View</button>

<button onclick="resendNotification(this)">Resend</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.mobileSection{
padding:90px 8%;
background:#f7fbff;
}

.mobileForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.mobileForm input,
.mobileForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.mobileForm button{
padding:15px;
background:#1976d2;
color:white;
border:none;
border-radius:10px;
font-weight:bold;
cursor:pointer;
}

.mobileCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.mobileCard{
background:white;
padding:30px;
text-align:center;
border-radius:20px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.mobileCard h1{
font-size:42px;
color:#1976d2;
}

.mobileTable{
width:100%;
border-collapse:collapse;
background:white;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.mobileTable th{
background:#1976d2;
color:white;
padding:15px;
}

.mobileTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.mobileSuccess{
background:#2e7d32;
color:white;
padding:6px 12px;
border-radius:20px;
}

.mobilePending{
background:#ef6c00;
color:white;
padding:6px 12px;
border-radius:20px;
}

.mobileTable button{
padding:8px 14px;
margin:2px;
background:#1976d2;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let notificationID=1;

function sendPushNotification(){

let patient=document.getElementById("mobilePatient").value;
let platform=document.getElementById("platform").value;
let type=document.getElementById("notificationType").value;

if(patient==""){

alert("Enter patient name.");

return;

}

notificationID++;

let now=new Date().toLocaleTimeString();

let row="<tr>"+
"<td>"+notificationID+"</td>"+
"<td>"+patient+"</td>"+
"<td>"+platform+"</td>"+
"<td>"+type+"</td>"+
"<td><span class='mobileSuccess'>Delivered</span></td>"+
"<td>"+now+"</td>"+
"<td><button onclick='viewNotification(this)'>View</button> <button onclick='resendNotification(this)'>Resend</button></td>"+
"</tr>";

document.getElementById("mobileBody").innerHTML+=row;

document.getElementById("totalNotifications").innerHTML=
parseInt(document.getElementById("totalNotifications").innerHTML)+1;

document.getElementById("successfulNotifications").innerHTML=
parseInt(document.getElementById("successfulNotifications").innerHTML)+1;

document.getElementById("apiRequests").innerHTML=
parseInt(document.getElementById("apiRequests").innerHTML)+1;

alert("📲 Push notification sent successfully.");

}

function viewNotification(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+

"\nPlatform : "+row.cells[2].innerHTML+

"\nNotification : "+row.cells[3].innerHTML+

"\nStatus : "+row.cells[4].innerText+

"\nTime : "+row.cells[5].innerHTML

);

}

function resendNotification(btn){

alert("🔔 Notification resent successfully.");

}

</script>
<!-- ================= WHATSAPP BUSINESS INTEGRATION ================= -->

<section class="whatsappSection">

<h2 class="title">💬 WhatsApp Business Integration</h2>

<div class="whatsappForm">

<input type="text" id="waPatient" placeholder="Patient Name">

<input type="tel" id="waNumber" placeholder="WhatsApp Number">

<select id="waMessageType">

<option>Appointment Reminder</option>
<option>Medicine Reminder</option>
<option>Lab Report Ready</option>
<option>Prescription PDF</option>
<option>Invoice & Payment Link</option>
<option>Emergency Alert</option>
<option>Doctor Consultation</option>

</select>

<textarea id="waMessage" placeholder="Enter WhatsApp Message"></textarea>

<button onclick="sendWhatsApp()">

💬 Send WhatsApp

</button>

</div>

<div class="waCards">

<div class="waCard">

<h1 id="waTotal">8654</h1>

<p>Total Messages</p>

</div>

<div class="waCard">

<h1 id="waDelivered">8521</h1>

<p>Delivered</p>

</div>

<div class="waCard">

<h1 id="waFailed">133</h1>

<p>Failed</p>

</div>

<div class="waCard">

<h1 id="waChatbot">2147</h1>

<p>AI Chatbot Replies</p>

</div>

</div>

<table class="waTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Mobile</th>

<th>Message Type</th>

<th>Status</th>

<th>Time</th>

<th>Action</th>

</tr>

</thead>

<tbody id="waBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>+91 9876543210</td>

<td>Appointment Reminder</td>

<td><span class="waSuccess">Delivered</span></td>

<td>11:20 AM</td>

<td>

<button onclick="viewWA(this)">View</button>

<button onclick="resendWA(this)">Resend</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.whatsappSection{

padding:90px 8%;

background:#f6fff7;

}

.whatsappForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.whatsappForm input,

.whatsappForm select,

.whatsappForm textarea{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

font-size:15px;

}

.whatsappForm textarea{

min-height:120px;

resize:vertical;

}

.whatsappForm button{

padding:15px;

background:#25D366;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.waCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.waCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.waCard h1{

font-size:40px;

color:#25D366;

}

.waTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.waTable th{

background:#25D366;

color:white;

padding:15px;

}

.waTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.waSuccess{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.waFailed{

background:#d32f2f;

color:white;

padding:6px 12px;

border-radius:20px;

}

.waTable button{

padding:8px 14px;

margin:2px;

background:#25D366;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let waID=1;

function sendWhatsApp(){

let patient=document.getElementById("waPatient").value;

let number=document.getElementById("waNumber").value;

let type=document.getElementById("waMessageType").value;

let message=document.getElementById("waMessage").value;

if(patient==""||number==""){

alert("Please enter patient details.");

return;

}

waID++;

let time=new Date().toLocaleTimeString();

let row="<tr>"+

"<td>"+waID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+number+"</td>"+

"<td>"+type+"</td>"+

"<td><span class='waSuccess'>Delivered</span></td>"+

"<td>"+time+"</td>"+

"<td><button onclick='viewWA(this)'>View</button> <button onclick='resendWA(this)'>Resend</button></td>"+

"</tr>";

document.getElementById("waBody").innerHTML+=row;

document.getElementById("waTotal").innerHTML=

parseInt(document.getElementById("waTotal").innerHTML)+1;

document.getElementById("waDelivered").innerHTML=

parseInt(document.getElementById("waDelivered").innerHTML)+1;

alert("💬 WhatsApp message sent successfully.");

}

function viewWA(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+

"\nMobile : "+row.cells[2].innerHTML+

"\nMessage : "+row.cells[3].innerHTML+

"\nStatus : "+row.cells[4].innerText+

"\nTime : "+row.cells[5].innerHTML

);

}

function resendWA(){

alert("🔄 WhatsApp message resent successfully.");

}

</script>
<!-- ================= EXECUTIVE BUSINESS INTELLIGENCE ================= -->

<section class="executiveSection">

<h2 class="title">📊 Executive Business Intelligence Dashboard</h2>

<div class="executiveFilters">

<select id="reportPeriod">

<option>Today</option>
<option>This Week</option>
<option>This Month</option>
<option>This Quarter</option>
<option>This Year</option>

</select>

<select id="hospitalBranch">

<option>All Branches</option>
<option>Chennai</option>
<option>Coimbatore</option>
<option>Madurai</option>
<option>Trichy</option>

</select>

<button onclick="generateExecutiveReport()">

Generate Dashboard

</button>

</div>

<div class="executiveCards">

<div class="executiveCard">

<h1 id="executiveRevenue">₹2.48 Cr</h1>

<p>Total Revenue</p>

</div>

<div class="executiveCard">

<h1 id="executiveProfit">₹82 Lakh</h1>

<p>Net Profit</p>

</div>

<div class="executiveCard">

<h1 id="executivePatients">18,542</h1>

<p>Total Patients</p>

</div>

<div class="executiveCard">

<h1 id="executiveDoctors">312</h1>

<p>Doctors</p>

</div>

<div class="executiveCard">

<h1 id="executiveBeds">94%</h1>

<p>Bed Occupancy</p>

</div>

<div class="executiveCard">

<h1 id="executiveSatisfaction">4.8/5</h1>

<p>Patient Satisfaction</p>

</div>

</div>

<table class="executiveTable">

<thead>

<tr>

<th>KPI</th>

<th>Current</th>

<th>Previous</th>

<th>Growth</th>

<th>Status</th>

</tr>

</thead>

<tbody id="executiveBody">

<tr>

<td>Revenue</td>

<td>₹2.48 Cr</td>

<td>₹2.21 Cr</td>

<td>+12%</td>

<td><span class="positive">Excellent</span></td>

</tr>

<tr>

<td>OPD Visits</td>

<td>9,430</td>

<td>8,790</td>

<td>+7%</td>

<td><span class="positive">Growing</span></td>

</tr>

<tr>

<td>IPD Admissions</td>

<td>2,180</td>

<td>2,050</td>

<td>+6%</td>

<td><span class="positive">Stable</span></td>

</tr>

<tr>

<td>Pharmacy Sales</td>

<td>₹42 Lakh</td>

<td>₹39 Lakh</td>

<td>+8%</td>

<td><span class="positive">Excellent</span></td>

</tr>

<tr>

<td>Lab Revenue</td>

<td>₹18 Lakh</td>

<td>₹16 Lakh</td>

<td>+11%</td>

<td><span class="positive">Growing</span></td>

</tr>

</tbody>

</table>

<div class="aiInsights">

<h3>🤖 AI Executive Insights</h3>

<ul id="insightList">

<li>✅ Revenue increased by 12% compared to the previous period.</li>

<li>🏥 Bed occupancy reached 94%; expansion planning recommended.</li>

<li>👨‍⚕️ Cardiology department has the highest patient volume.</li>

<li>💊 Pharmacy sales continue to show steady growth.</li>

<li>😊 Patient satisfaction remains above 4.8/5.</li>

</ul>

</div>

</section>

<style>

.executiveSection{
padding:90px 8%;
background:#f5f9ff;
}

.executiveFilters{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.executiveFilters select,
.executiveFilters button{
padding:15px;
border-radius:10px;
border:1px solid #ccc;
}

.executiveFilters button{
background:#1a237e;
color:white;
border:none;
cursor:pointer;
font-weight:bold;
}

.executiveCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
gap:20px;
margin-bottom:30px;
}

.executiveCard{
background:white;
padding:30px;
text-align:center;
border-radius:18px;
box-shadow:0 8px 18px rgba(0,0,0,.08);
}

.executiveCard h1{
font-size:38px;
color:#1a237e;
}

.executiveTable{
width:100%;
border-collapse:collapse;
background:white;
border-radius:15px;
overflow:hidden;
box-shadow:0 8px 18px rgba(0,0,0,.08);
margin-bottom:30px;
}

.executiveTable th{
background:#1a237e;
color:white;
padding:15px;
}

.executiveTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.positive{
background:#2e7d32;
color:white;
padding:6px 12px;
border-radius:20px;
}

.aiInsights{
background:white;
padding:25px;
border-radius:18px;
box-shadow:0 8px 18px rgba(0,0,0,.08);
}

.aiInsights h3{
color:#1a237e;
margin-bottom:15px;
}

.aiInsights ul{
padding-left:20px;
line-height:2;
}

</style>

<script>

function generateExecutiveReport(){

let period=document.getElementById("reportPeriod").value;

let branch=document.getElementById("hospitalBranch").value;

alert(
"📊 Executive Dashboard Generated\n\n"+
"Period : "+period+
"\nBranch : "+branch+
"\n\nReport generated successfully."
);

}

</script>
<!-- ================= MULTI LANGUAGE & LOCALIZATION ================= -->

<section class="languageSection">

<h2 class="title">🌍 Multi-Language & Localization</h2>

<div class="languageForm">

<select id="languageSelect">

<option value="en">🇺🇸 English</option>
<option value="ta">🇮🇳 Tamil</option>
<option value="hi">🇮🇳 Hindi</option>
<option value="ar">🇸🇦 Arabic (RTL)</option>
<option value="fr">🇫🇷 French</option>
<option value="es">🇪🇸 Spanish</option>

</select>

<select id="currencySelect">

<option>₹ INR</option>
<option>$ USD</option>
<option>€ EUR</option>
<option>£ GBP</option>

</select>

<select id="dateFormat">

<option>DD/MM/YYYY</option>
<option>MM/DD/YYYY</option>
<option>YYYY-MM-DD</option>

</select>

<button onclick="applyLocalization()">

🌍 Apply Settings

</button>

</div>

<div class="languageCards">

<div class="languageCard">

<h1 id="supportedLanguages">25</h1>

<p>Supported Languages</p>

</div>

<div class="languageCard">

<h1 id="activeUsers">1248</h1>

<p>Localized Users</p>

</div>

<div class="languageCard">

<h1 id="rtlLanguages">4</h1>

<p>RTL Languages</p>

</div>

<div class="languageCard">

<h1 id="translations">98%</h1>

<p>Translation Coverage</p>

</div>

</div>

<table class="languageTable">

<thead>

<tr>

<th>ID</th>

<th>Language</th>

<th>Currency</th>

<th>Date Format</th>

<th>Direction</th>

<th>Status</th>

</tr>

</thead>

<tbody id="languageBody">

<tr>

<td>1</td>

<td>English</td>

<td>₹ INR</td>

<td>DD/MM/YYYY</td>

<td>LTR</td>

<td><span class="activeLang">Active</span></td>

</tr>

</tbody>

</table>

<div class="previewBox">

<h3 id="previewTitle">Hospital Management System</h3>

<p id="previewText">

Welcome to the Hospital Management System.

</p>

</div>

</section>

<style>

.languageSection{

padding:90px 8%;

background:#f7fcff;

}

.languageForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.languageForm select,

.languageForm button{

padding:15px;

border-radius:10px;

border:1px solid #ccc;

}

.languageForm button{

background:#1565c0;

color:white;

border:none;

cursor:pointer;

font-weight:bold;

}

.languageCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.languageCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.languageCard h1{

font-size:42px;

color:#1565c0;

}

.languageTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

margin-bottom:30px;

}

.languageTable th{

background:#1565c0;

color:white;

padding:15px;

}

.languageTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.activeLang{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.previewBox{

background:white;

padding:25px;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

text-align:center;

}

</style>

<script>

const translations={

en:{
title:"Hospital Management System",
text:"Welcome to the Hospital Management System."
},

ta:{
title:"மருத்துவமனை மேலாண்மை அமைப்பு",
text:"மருத்துவமனை மேலாண்மை அமைப்பிற்கு வரவேற்கிறோம்."
},

hi:{
title:"अस्पताल प्रबंधन प्रणाली",
text:"अस्पताल प्रबंधन प्रणाली में आपका स्वागत है।"
},

ar:{
title:"نظام إدارة المستشفى",
text:"مرحبًا بك في نظام إدارة المستشفى."
},

fr:{
title:"Système de Gestion Hospitalière",
text:"Bienvenue dans le système de gestion hospitalière."
},

es:{
title:"Sistema de Gestión Hospitalaria",
text:"Bienvenido al sistema de gestión hospitalaria."
}

};

let languageID=1;

function applyLocalization(){

let lang=document.getElementById("languageSelect").value;

let currency=document.getElementById("currencySelect").value;

let date=document.getElementById("dateFormat").value;

let dir=(lang==="ar")?"rtl":"ltr";

document.body.dir=dir;

document.getElementById("previewTitle").innerHTML=
translations[lang].title;

document.getElementById("previewText").innerHTML=
translations[lang].text;

languageID++;

let row="<tr>"+

"<td>"+languageID+"</td>"+

"<td>"+document.getElementById("languageSelect").options[document.getElementById("languageSelect").selectedIndex].text+"</td>"+

"<td>"+currency+"</td>"+

"<td>"+date+"</td>"+

"<td>"+dir.toUpperCase()+"</td>"+

"<td><span class='activeLang'>Applied</span></td>"+

"</tr>";

document.getElementById("languageBody").innerHTML+=row;

document.getElementById("activeUsers").innerHTML=
parseInt(document.getElementById("activeUsers").innerHTML)+1;

alert("🌍 Localization applied successfully.");

}

</script>
<!-- ================= AI HOSPITAL COMMAND CENTER ================= -->

<section class="commandSection">

<h2 class="title">🤖 AI Hospital Command Center</h2>

<div class="commandActions">

<button onclick="runAIAnalysis()">🧠 Run AI Analysis</button>

<button onclick="predictPatientFlow()">📈 Predict Patient Flow</button>

<button onclick="forecastRevenue()">💰 Forecast Revenue</button>

<button onclick="optimizeHospital()">⚙️ Optimize Hospital</button>

</div>

<div class="commandCards">

<div class="commandCard">
<h1 id="hospitalHealth">98%</h1>
<p>Hospital Health Score</p>
</div>

<div class="commandCard">
<h1 id="livePatients">486</h1>
<p>Live Patients</p>
</div>

<div class="commandCard">
<h1 id="availableBeds">72</h1>
<p>Available Beds</p>
</div>

<div class="commandCard">
<h1 id="criticalCases">11</h1>
<p>Critical Cases</p>
</div>

<div class="commandCard">
<h1 id="doctorLoad">83%</h1>
<p>Doctor Utilization</p>
</div>

<div class="commandCard">
<h1 id="aiConfidence">97%</h1>
<p>AI Confidence</p>
</div>

</div>

<table class="commandTable">

<thead>

<tr>

<th>Module</th>
<th>Status</th>
<th>AI Analysis</th>
<th>Recommendation</th>

</tr>

</thead>

<tbody id="commandBody">

<tr>

<td>Emergency</td>

<td>🟢 Normal</td>

<td>Patient volume stable</td>

<td>Maintain staffing</td>

</tr>

<tr>

<td>ICU</td>

<td>🟡 Busy</td>

<td>Occupancy above 90%</td>

<td>Add 2 ICU beds</td>

</tr>

<tr>

<td>Pharmacy</td>

<td>🟢 Healthy</td>

<td>No shortages detected</td>

<td>Continue monitoring</td>

</tr>

<tr>

<td>Laboratory</td>

<td>🟢 Normal</td>

<td>Average turnaround time</td>

<td>No action required</td>

</tr>

<tr>

<td>Billing</td>

<td>🟢 Good</td>

<td>Collections on target</td>

<td>Monitor pending invoices</td>

</tr>

</tbody>

</table>

<div class="recommendationBox">

<h3>🤖 AI Recommendations</h3>

<ul id="recommendations">

<li>🏥 ICU occupancy is high. Prepare additional beds.</li>

<li>👨‍⚕️ Schedule one additional cardiologist for evening shift.</li>

<li>💊 Restock emergency medicines within 48 hours.</li>

<li>🚑 Ambulance response time is within target.</li>

<li>📈 Expected OPD increase tomorrow: +12%.</li>

</ul>

</div>

</section>

<style>

.commandSection{

padding:90px 8%;

background:#f4f8ff;

}

.commandActions{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.commandActions button{

padding:16px;

background:#283593;

color:white;

border:none;

border-radius:12px;

font-weight:bold;

cursor:pointer;

}

.commandCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(180px,1fr));

gap:20px;

margin-bottom:30px;

}

.commandCard{

background:white;

padding:30px;

text-align:center;

border-radius:18px;

box-shadow:0 10px 18px rgba(0,0,0,.08);

}

.commandCard h1{

font-size:38px;

color:#283593;

}

.commandTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 18px rgba(0,0,0,.08);

margin-bottom:30px;

}

.commandTable th{

background:#283593;

color:white;

padding:15px;

}

.commandTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.recommendationBox{

background:white;

padding:25px;

border-radius:18px;

box-shadow:0 10px 18px rgba(0,0,0,.08);

}

.recommendationBox h3{

color:#283593;

margin-bottom:15px;

}

.recommendationBox ul{

line-height:2;

padding-left:20px;

}

</style>

<script>

function runAIAnalysis(){

alert("🧠 AI analyzed all hospital modules successfully.");

document.getElementById("hospitalHealth").innerHTML="99%";

document.getElementById("aiConfidence").innerHTML="98%";

}

function predictPatientFlow(){

alert("📈 AI predicts approximately 540 patient visits tomorrow (+12%).");

}

function forecastRevenue(){

alert("💰 Estimated monthly revenue: ₹2.75 Crore");

}

function optimizeHospital(){

let list=document.getElementById("recommendations");

let item=document.createElement("li");

item.innerHTML="✅ AI optimized staff allocation, ICU resources, pharmacy inventory and appointment scheduling.";

list.appendChild(item);

alert("⚙️ Hospital optimization completed.");

}

</script>
<!-- ================= CLINICAL RESEARCH ================= -->

<section class="researchSection">

<h2 class="title">🧬 Clinical Research & Trial Management</h2>

<div class="researchForm">

<input type="text" id="studyName" placeholder="Clinical Study Name">

<input type="text" id="principalInvestigator" placeholder="Principal Investigator">

<select id="trialPhase">

<option>Phase I</option>
<option>Phase II</option>
<option>Phase III</option>
<option>Phase IV</option>

</select>

<select id="trialStatus">

<option>Planning</option>
<option>Recruiting</option>
<option>Active</option>
<option>Completed</option>

</select>

<input type="number" id="participantCount" placeholder="Participants">

<button onclick="registerTrial()">

🧬 Register Trial

</button>

</div>

<div class="researchCards">

<div class="researchCard">

<h1 id="totalTrials">28</h1>

<p>Clinical Trials</p>

</div>

<div class="researchCard">

<h1 id="activeTrials">16</h1>

<p>Active Trials</p>

</div>

<div class="researchCard">

<h1 id="participants">1248</h1>

<p>Participants</p>

</div>

<div class="researchCard">

<h1 id="ethicsApproval">96%</h1>

<p>Ethics Approval</p>

</div>

</div>

<table class="researchTable">

<thead>

<tr>

<th>ID</th>

<th>Study</th>

<th>Phase</th>

<th>Investigator</th>

<th>Status</th>

<th>Participants</th>

<th>Action</th>

</tr>

</thead>

<tbody id="researchBody">

<tr>

<td>1</td>

<td>Diabetes AI Study</td>

<td>Phase III</td>

<td>Dr. Sharma</td>

<td><span class="trialActive">Active</span></td>

<td>180</td>

<td>

<button onclick="viewTrial(this)">View</button>

<button onclick="approveTrial(this)">Approve</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.researchSection{
padding:90px 8%;
background:#f9fcff;
}

.researchForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.researchForm input,
.researchForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.researchForm button{
padding:15px;
background:#6a1b9a;
color:white;
border:none;
border-radius:10px;
cursor:pointer;
font-weight:bold;
}

.researchCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.researchCard{
background:white;
padding:30px;
text-align:center;
border-radius:20px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.researchCard h1{
font-size:42px;
color:#6a1b9a;
}

.researchTable{
width:100%;
border-collapse:collapse;
background:white;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.researchTable th{
background:#6a1b9a;
color:white;
padding:15px;
}

.researchTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.trialActive{
background:#2e7d32;
color:white;
padding:6px 12px;
border-radius:20px;
}

.trialPending{
background:#ef6c00;
color:white;
padding:6px 12px;
border-radius:20px;
}

.researchTable button{
padding:8px 14px;
margin:2px;
background:#6a1b9a;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let trialID=1;

function registerTrial(){

let study=document.getElementById("studyName").value;

let investigator=document.getElementById("principalInvestigator").value;

let phase=document.getElementById("trialPhase").value;

let status=document.getElementById("trialStatus").value;

let people=parseInt(document.getElementById("participantCount").value)||0;

if(study==""||investigator==""){

alert("Please complete required fields.");

return;

}

trialID++;

let badge="<span class='trialPending'>"+status+"</span>";

if(status=="Active"){

badge="<span class='trialActive'>Active</span>";

document.getElementById("activeTrials").innerHTML=

parseInt(document.getElementById("activeTrials").innerHTML)+1;

}

let row="<tr>"+

"<td>"+trialID+"</td>"+

"<td>"+study+"</td>"+

"<td>"+phase+"</td>"+

"<td>"+investigator+"</td>"+

"<td>"+badge+"</td>"+

"<td>"+people+"</td>"+

"<td><button onclick='viewTrial(this)'>View</button> <button onclick='approveTrial(this)'>Approve</button></td>"+

"</tr>";

document.getElementById("researchBody").innerHTML+=row;

document.getElementById("totalTrials").innerHTML=

parseInt(document.getElementById("totalTrials").innerHTML)+1;

document.getElementById("participants").innerHTML=

parseInt(document.getElementById("participants").innerHTML)+people;

alert("🧬 Clinical trial registered successfully.");

}

function viewTrial(btn){

let row=btn.parentElement.parentElement;

alert(

"Study : "+row.cells[1].innerHTML+

"\nPhase : "+row.cells[2].innerHTML+

"\nPrincipal Investigator : "+row.cells[3].innerHTML+

"\nStatus : "+row.cells[4].innerText+

"\nParticipants : "+row.cells[5].innerHTML

);

}

function approveTrial(btn){

let row=btn.parentElement.parentElement;

row.cells[4].innerHTML="<span class='trialActive'>Approved</span>";

alert("✅ Ethics Committee approval recorded.");

}

</script>
<!-- ================= DIGITAL SIGNATURE & E-PRESCRIPTION ================= -->

<section class="eprescriptionSection">

<h2 class="title">🧾 Digital Signature & e-Prescription</h2>

<div class="eprescriptionForm">

<input type="text" id="doctorName" placeholder="Doctor Name">

<input type="text" id="doctorLicense" placeholder="Medical License Number">

<input type="text" id="patientName" placeholder="Patient Name">

<textarea id="medicineList" placeholder="Prescription Details"></textarea>

<select id="signatureType">

<option>Digital Signature</option>

<option>Electronic Signature</option>

<option>Verified Certificate</option>

</select>

<button onclick="generatePrescription()">

💊 Generate Prescription

</button>

</div>

<div class="epCards">

<div class="epCard">

<h1 id="totalPrescriptions">4520</h1>

<p>Total Prescriptions</p>

</div>

<div class="epCard">

<h1 id="signedPrescriptions">4472</h1>

<p>Digitally Signed</p>

</div>

<div class="epCard">

<h1 id="verifiedDoctors">248</h1>

<p>Verified Doctors</p>

</div>

<div class="epCard">

<h1 id="qrVerified">4398</h1>

<p>QR Verified</p>

</div>

</div>

<table class="epTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Doctor</th>

<th>License</th>

<th>Signature</th>

<th>QR</th>

<th>Action</th>

</tr>

</thead>

<tbody id="epBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Dr. Kumar</td>

<td>TNMC10245</td>

<td><span class="signed">Signed</span></td>

<td>Verified</td>

<td>

<button onclick="viewPrescription(this)">View</button>

<button onclick="downloadPrescription(this)">PDF</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.eprescriptionSection{

padding:90px 8%;

background:#f8fcff;

}

.eprescriptionForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.eprescriptionForm input,

.eprescriptionForm textarea,

.eprescriptionForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.eprescriptionForm textarea{

min-height:120px;

resize:vertical;

}

.eprescriptionForm button{

padding:15px;

background:#1565c0;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.epCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.epCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.epCard h1{

font-size:40px;

color:#1565c0;

}

.epTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.epTable th{

background:#1565c0;

color:white;

padding:15px;

}

.epTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.signed{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.epTable button{

padding:8px 14px;

margin:2px;

background:#1565c0;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let prescriptionID=1;

function generatePrescription(){

let doctor=document.getElementById("doctorName").value;

let license=document.getElementById("doctorLicense").value;

let patient=document.getElementById("patientName").value;

let medicine=document.getElementById("medicineList").value;

let sign=document.getElementById("signatureType").value;

if(doctor==""||patient==""||medicine==""){

alert("Please complete all required fields.");

return;

}

prescriptionID++;

let row="<tr>"+

"<td>"+prescriptionID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+doctor+"</td>"+

"<td>"+license+"</td>"+

"<td><span class='signed'>"+sign+"</span></td>"+

"<td>Verified</td>"+

"<td><button onclick='viewPrescription(this)'>View</button> <button onclick='downloadPrescription(this)'>PDF</button></td>"+

"</tr>";

document.getElementById("epBody").innerHTML+=row;

document.getElementById("totalPrescriptions").innerHTML=

parseInt(document.getElementById("totalPrescriptions").innerHTML)+1;

document.getElementById("signedPrescriptions").innerHTML=

parseInt(document.getElementById("signedPrescriptions").innerHTML)+1;

alert("🧾 Electronic prescription generated successfully.");

}

function viewPrescription(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+

"\nDoctor : "+row.cells[2].innerHTML+

"\nLicense : "+row.cells[3].innerHTML+

"\nSignature : "+row.cells[4].innerText+

"\nQR Verification : "+row.cells[5].innerHTML

);

}

function downloadPrescription(){

alert("📄 PDF prescription downloaded successfully.");

}

</script>
<!-- ================= AI MEDICAL DECISION SUPPORT SYSTEM ================= -->

<section class="mdssSection">

<h2 class="title">🧠 AI Medical Decision Support System (MDSS)</h2>

<div class="mdssForm">

<input type="text" id="patientName" placeholder="Patient Name">

<input type="number" id="patientAge" placeholder="Age">

<input type="text" id="patientSymptoms" placeholder="Symptoms (comma separated)">

<input type="text" id="patientAllergy" placeholder="Known Allergies">

<select id="labStatus">

<option>Normal</option>
<option>Abnormal</option>
<option>Critical</option>

</select>

<button onclick="analyzePatient()">

🧠 Analyze Patient

</button>

</div>

<div class="mdssCards">

<div class="mdssCard">

<h1 id="analysisCount">6248</h1>

<p>AI Analyses</p>

</div>

<div class="mdssCard">

<h1 id="criticalCases">112</h1>

<p>Critical Cases</p>

</div>

<div class="mdssCard">

<h1 id="drugAlerts">48</h1>

<p>Drug Alerts</p>

</div>

<div class="mdssCard">

<h1 id="aiAccuracy">97%</h1>

<p>AI Confidence</p>

</div>

</div>

<table class="mdssTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Risk</th>

<th>Diagnosis Suggestion</th>

<th>Recommendation</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="mdssBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Medium</td>

<td>Possible Viral Infection</td>

<td>Doctor Review</td>

<td><span class="review">Pending</span></td>

<td>

<button onclick="viewDecision(this)">View</button>

<button onclick="approveDecision(this)">Approve</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.mdssSection{

padding:90px 8%;

background:#f7fbff;

}

.mdssForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.mdssForm input,

.mdssForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.mdssForm button{

padding:15px;

background:#0d47a1;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.mdssCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.mdssCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.mdssCard h1{

font-size:40px;

color:#0d47a1;

}

.mdssTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.mdssTable th{

background:#0d47a1;

color:white;

padding:15px;

}

.mdssTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.review{

background:#fb8c00;

color:white;

padding:6px 12px;

border-radius:20px;

}

.approved{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.mdssTable button{

padding:8px 14px;

margin:2px;

background:#0d47a1;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let decisionID=1;

function analyzePatient(){

let patient=document.getElementById("patientName").value;

let symptoms=document.getElementById("patientSymptoms").value.toLowerCase();

let allergy=document.getElementById("patientAllergy").value.toLowerCase();

let lab=document.getElementById("labStatus").value;

if(patient==""){

alert("Please enter patient details.");

return;

}

let diagnosis="General Checkup";

let risk="Low";

let recommendation="Routine Follow-up";

if(symptoms.includes("fever") && symptoms.includes("cough")){

diagnosis="Possible Viral Infection";

risk="Medium";

recommendation="Doctor Evaluation";

}

if(symptoms.includes("chest")){

diagnosis="Possible Cardiac Condition";

risk="High";

recommendation="Immediate Cardiology Review";

}

if(lab=="Critical"){

risk="Critical";

recommendation="Emergency Admission";

}

if(allergy.includes("penicillin")){

document.getElementById("drugAlerts").innerHTML=

parseInt(document.getElementById("drugAlerts").innerHTML)+1;

}

decisionID++;

let row="<tr>"+

"<td>"+decisionID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+risk+"</td>"+

"<td>"+diagnosis+"</td>"+

"<td>"+recommendation+"</td>"+

"<td><span class='review'>Pending</span></td>"+

"<td><button onclick='viewDecision(this)'>View</button> <button onclick='approveDecision(this)'>Approve</button></td>"+

"</tr>";

document.getElementById("mdssBody").innerHTML+=row;

document.getElementById("analysisCount").innerHTML=

parseInt(document.getElementById("analysisCount").innerHTML)+1;

if(risk=="Critical"){

document.getElementById("criticalCases").innerHTML=

parseInt(document.getElementById("criticalCases").innerHTML)+1;

}

alert("🧠 AI clinical decision generated.");

}

function approveDecision(btn){

let row=btn.parentElement.parentElement;

row.cells[5].innerHTML="<span class='approved'>Approved</span>";

alert("✅ Doctor approved AI recommendation.");

}

function viewDecision(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+

"\nRisk : "+row.cells[2].innerHTML+

"\nDiagnosis : "+row.cells[3].innerHTML+

"\nRecommendation : "+row.cells[4].innerHTML+

"\n\n⚠ AI recommendations are for clinical support only. Final diagnosis and treatment decisions must be made by a qualified healthcare professional."

);

}

</script><!-- ================= DENTAL MANAGEMENT SYSTEM ================= -->

<section class="dentalSection">

<h2 class="title">🦷 Dental Management System</h2>

<div class="dentalForm">

<input type="text" id="patientName" placeholder="Patient Name">

<input type="number" id="patientAge" placeholder="Age">

<select id="toothNumber">

<option>Tooth 11</option>
<option>Tooth 12</option>
<option>Tooth 13</option>
<option>Tooth 14</option>
<option>Tooth 21</option>
<option>Tooth 22</option>
<option>Tooth 23</option>
<option>Tooth 24</option>
<option>Tooth 31</option>
<option>Tooth 32</option>
<option>Tooth 33</option>
<option>Tooth 34</option>
<option>Tooth 41</option>
<option>Tooth 42</option>
<option>Tooth 43</option>
<option>Tooth 44</option>

</select>

<select id="treatment">

<option>Dental Checkup</option>
<option>Cleaning</option>
<option>Root Canal</option>
<option>Tooth Extraction</option>
<option>Dental Filling</option>
<option>Dental Crown</option>
<option>Dental Implant</option>
<option>Orthodontic Braces</option>

</select>

<button onclick="addDentalRecord()">

🦷 Save Record

</button>

</div>

<div class="dentalCards">

<div class="dentalCard">

<h1 id="totalDentalPatients">1452</h1>

<p>Dental Patients</p>

</div>

<div class="dentalCard">

<h1 id="todayAppointments">48</h1>

<p>Today's Appointments</p>

</div>

<div class="dentalCard">

<h1 id="completedTreatments">1187</h1>

<p>Treatments Completed</p>

</div>

<div class="dentalCard">

<h1 id="implantCases">142</h1>

<p>Implant Cases</p>

</div>

</div>

<table class="dentalTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Tooth</th>

<th>Treatment</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="dentalBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Tooth 21</td>

<td>Cleaning</td>

<td><span class="completed">Completed</span></td>

<td>

<button onclick="viewDental(this)">View</button>

<button onclick="printDental(this)">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.dentalSection{

padding:90px 8%;

background:#f7fcff;

}

.dentalForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.dentalForm input,
.dentalForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.dentalForm button{

padding:15px;

background:#0097a7;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.dentalCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.dentalCard{

background:white;

padding:30px;

text-align:center;

border-radius:18px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.dentalCard h1{

font-size:40px;

color:#0097a7;

}

.dentalTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.dentalTable th{

background:#0097a7;

color:white;

padding:15px;

}

.dentalTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.completed{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.dentalTable button{

padding:8px 14px;

margin:2px;

background:#0097a7;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let dentalID=1;

function addDentalRecord(){

let patient=document.getElementById("patientName").value;

let tooth=document.getElementById("toothNumber").value;

let treatment=document.getElementById("treatment").value;

if(patient==""){

alert("Please enter patient name.");

return;

}

dentalID++;

let row="<tr>"+

"<td>"+dentalID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+tooth+"</td>"+

"<td>"+treatment+"</td>"+

"<td><span class='completed'>Scheduled</span></td>"+

"<td><button onclick='viewDental(this)'>View</button> <button onclick='printDental(this)'>Print</button></td>"+

"</tr>";

document.getElementById("dentalBody").innerHTML+=row;

document.getElementById("totalDentalPatients").innerHTML=

parseInt(document.getElementById("totalDentalPatients").innerHTML)+1;

alert("🦷 Dental record added successfully.");

}

function viewDental(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+

"\nTooth : "+row.cells[2].innerHTML+

"\nTreatment : "+row.cells[3].innerHTML+

"\nStatus : "+row.cells[4].innerText

);

}

function printDental(){

window.print();

}

</script>
<!-- ================= OPHTHALMOLOGY MANAGEMENT SYSTEM ================= -->

<section class="eyeSection">

<h2 class="title">👁️ Ophthalmology Management</h2>

<div class="eyeForm">

<input type="text" id="eyePatient" placeholder="Patient Name">

<input type="number" id="eyeAge" placeholder="Age">

<select id="eyeCondition">

<option>Normal Checkup</option>
<option>Myopia</option>
<option>Hyperopia</option>
<option>Astigmatism</option>
<option>Cataract</option>
<option>Glaucoma</option>
<option>Diabetic Retinopathy</option>

</select>

<select id="eyeTreatment">

<option>Eye Examination</option>
<option>Prescription Glasses</option>
<option>Contact Lens</option>
<option>Cataract Surgery</option>
<option>Laser Surgery</option>
<option>Retina Treatment</option>

</select>

<button onclick="addEyeRecord()">

👁️ Save Record

</button>

</div>

<div class="eyeCards">

<div class="eyeCard">

<h1 id="eyePatients">2548</h1>

<p>Eye Patients</p>

</div>

<div class="eyeCard">

<h1 id="visionTests">1832</h1>

<p>Vision Tests</p>

</div>

<div class="eyeCard">

<h1 id="eyeSurgeries">286</h1>

<p>Eye Surgeries</p>

</div>

<div class="eyeCard">

<h1 id="retinaScans">964</h1>

<p>Retina Scans</p>

</div>

</div>

<table class="eyeTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Condition</th>

<th>Treatment</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="eyeBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Myopia</td>

<td>Prescription Glasses</td>

<td><span class="eyeCompleted">Completed</span></td>

<td>

<button onclick="viewEye(this)">View</button>

<button onclick="printEye()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.eyeSection{

padding:90px 8%;

background:#f6fcff;

}

.eyeForm{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:15px;

margin-bottom:30px;

}

.eyeForm input,
.eyeForm select{

padding:15px;

border:1px solid #ccc;

border-radius:10px;

}

.eyeForm button{

padding:15px;

background:#1976d2;

color:white;

border:none;

border-radius:10px;

font-weight:bold;

cursor:pointer;

}

.eyeCards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

gap:20px;

margin-bottom:30px;

}

.eyeCard{

background:white;

padding:30px;

text-align:center;

border-radius:20px;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.eyeCard h1{

font-size:40px;

color:#1976d2;

}

.eyeTable{

width:100%;

border-collapse:collapse;

background:white;

border-radius:15px;

overflow:hidden;

box-shadow:0 10px 20px rgba(0,0,0,.08);

}

.eyeTable th{

background:#1976d2;

color:white;

padding:15px;

}

.eyeTable td{

padding:15px;

text-align:center;

border-bottom:1px solid #eee;

}

.eyeCompleted{

background:#2e7d32;

color:white;

padding:6px 12px;

border-radius:20px;

}

.eyeTable button{

padding:8px 14px;

margin:2px;

background:#1976d2;

color:white;

border:none;

border-radius:8px;

cursor:pointer;

}

</style>

<script>

let eyeID=1;

function addEyeRecord(){

let patient=document.getElementById("eyePatient").value;

let condition=document.getElementById("eyeCondition").value;

let treatment=document.getElementById("eyeTreatment").value;

if(patient==""){

alert("Please enter patient name.");

return;

}

eyeID++;

let row="<tr>"+

"<td>"+eyeID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+condition+"</td>"+

"<td>"+treatment+"</td>"+

"<td><span class='eyeCompleted'>Scheduled</span></td>"+

"<td><button onclick='viewEye(this)'>View</button> <button onclick='printEye()'>Print</button></td>"+

"</tr>";

document.getElementById("eyeBody").innerHTML+=row;

document.getElementById("eyePatients").innerHTML=

parseInt(document.getElementById("eyePatients").innerHTML)+1;

alert("👁️ Eye care record added successfully.");

}

function viewEye(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+

"\nCondition : "+row.cells[2].innerHTML+

"\nTreatment : "+row.cells[3].innerHTML+

"\nStatus : "+row.cells[4].innerText

);

}

function printEye(){

window.print();

}

</script>
<!-- ================= MENTAL HEALTH & PSYCHIATRY MANAGEMENT ================= -->

<section class="mentalSection">

<h2 class="title">🧠 Mental Health & Psychiatry Management</h2>

<div class="mentalForm">

<input type="text" id="mentalPatient" placeholder="Patient Name">

<input type="number" id="mentalAge" placeholder="Age">

<select id="mentalAssessment">

<option>General Assessment</option>
<option>Depression Screening</option>
<option>Anxiety Screening</option>
<option>Bipolar Disorder</option>
<option>PTSD Assessment</option>
<option>OCD Assessment</option>
<option>Schizophrenia Evaluation</option>

</select>

<select id="therapyPlan">

<option>Counseling</option>
<option>Cognitive Behavioral Therapy</option>
<option>Psychotherapy</option>
<option>Medication Management</option>
<option>Group Therapy</option>
<option>Family Therapy</option>

</select>

<button onclick="saveMentalRecord()">

🧠 Save Assessment

</button>

</div>

<div class="mentalCards">

<div class="mentalCard">

<h1 id="mentalPatients">845</h1>

<p>Registered Patients</p>

</div>

<div class="mentalCard">

<h1 id="therapySessions">2864</h1>

<p>Therapy Sessions</p>

</div>

<div class="mentalCard">

<h1 id="highRiskCases">27</h1>

<p>High Risk Cases</p>

</div>

<div class="mentalCard">

<h1 id="psychiatrists">18</h1>

<p>Psychiatrists</p>

</div>

</div>

<table class="mentalTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Assessment</th>

<th>Therapy</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="mentalBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Anxiety Screening</td>

<td>CBT</td>

<td><span class="activeCase">In Progress</span></td>

<td>

<button onclick="viewMental(this)">View</button>

<button onclick="printMental()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.mentalSection{
padding:90px 8%;
background:#f8fbff;
}

.mentalForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.mentalForm input,
.mentalForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.mentalForm button{
padding:15px;
background:#6a1b9a;
color:white;
border:none;
border-radius:10px;
font-weight:bold;
cursor:pointer;
}

.mentalCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.mentalCard{
background:white;
padding:30px;
text-align:center;
border-radius:20px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.mentalCard h1{
font-size:40px;
color:#6a1b9a;
}

.mentalTable{
width:100%;
border-collapse:collapse;
background:white;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.mentalTable th{
background:#6a1b9a;
color:white;
padding:15px;
}

.mentalTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.activeCase{
background:#2e7d32;
color:white;
padding:6px 12px;
border-radius:20px;
}

.mentalTable button{
padding:8px 14px;
margin:2px;
background:#6a1b9a;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let mentalID=1;

function saveMentalRecord(){

let patient=document.getElementById("mentalPatient").value;
let assessment=document.getElementById("mentalAssessment").value;
let therapy=document.getElementById("therapyPlan").value;

if(patient==""){
alert("Please enter patient name.");
return;
}

mentalID++;

let row="<tr>"+
"<td>"+mentalID+"</td>"+
"<td>"+patient+"</td>"+
"<td>"+assessment+"</td>"+
"<td>"+therapy+"</td>"+
"<td><span class='activeCase'>Scheduled</span></td>"+
"<td><button onclick='viewMental(this)'>View</button> <button onclick='printMental()'>Print</button></td>"+
"</tr>";

document.getElementById("mentalBody").innerHTML+=row;

document.getElementById("mentalPatients").innerHTML=
parseInt(document.getElementById("mentalPatients").innerHTML)+1;

alert("🧠 Mental health assessment saved successfully.");

}

function viewMental(btn){

let row=btn.parentElement.parentElement;

alert(
"Patient : "+row.cells[1].innerHTML+
"\nAssessment : "+row.cells[2].innerHTML+
"\nTherapy : "+row.cells[3].innerHTML+
"\nStatus : "+row.cells[4].innerText
);

}

function printMental(){

window.print();

}

</script>
<!-- ================= REHABILITATION & PHYSIOTHERAPY MANAGEMENT ================= -->

<section class="rehabSection">

<h2 class="title">🦴 Rehabilitation & Physiotherapy Management</h2>

<div class="rehabForm">

<input type="text" id="rehabPatient" placeholder="Patient Name">

<input type="number" id="rehabAge" placeholder="Age">

<select id="rehabCondition">

<option>Post Surgery Rehabilitation</option>
<option>Sports Injury</option>
<option>Back Pain</option>
<option>Neck Pain</option>
<option>Stroke Rehabilitation</option>
<option>Fracture Recovery</option>
<option>Arthritis</option>
<option>Joint Replacement</option>

</select>

<select id="therapyType">

<option>Exercise Therapy</option>
<option>Manual Therapy</option>
<option>Electrotherapy</option>
<option>Hydrotherapy</option>
<option>Balance Training</option>
<option>Strength Training</option>
<option>Gait Training</option>

</select>

<input type="number" id="painScore" min="0" max="10" placeholder="Pain Score (0-10)">

<button onclick="saveRehabRecord()">

🦴 Save Rehabilitation Plan

</button>

</div>

<div class="rehabCards">

<div class="rehabCard">

<h1 id="rehabPatients">1368</h1>

<p>Patients</p>

</div>

<div class="rehabCard">

<h1 id="therapySessions">5924</h1>

<p>Therapy Sessions</p>

</div>

<div class="rehabCard">

<h1 id="recoveryRate">91%</h1>

<p>Recovery Rate</p>

</div>

<div class="rehabCard">

<h1 id="activePlans">347</h1>

<p>Active Plans</p>

</div>

</div>

<table class="rehabTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Condition</th>

<th>Therapy</th>

<th>Pain</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="rehabBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Sports Injury</td>

<td>Exercise Therapy</td>

<td>4/10</td>

<td><span class="progressStatus">In Progress</span></td>

<td>

<button onclick="viewRehab(this)">View</button>

<button onclick="printRehab()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.rehabSection{
padding:90px 8%;
background:#f5fcf8;
}

.rehabForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.rehabForm input,
.rehabForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.rehabForm button{
padding:15px;
background:#2e7d32;
color:white;
border:none;
border-radius:10px;
font-weight:bold;
cursor:pointer;
}

.rehabCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.rehabCard{
background:white;
padding:30px;
text-align:center;
border-radius:18px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.rehabCard h1{
font-size:40px;
color:#2e7d32;
}

.rehabTable{
width:100%;
border-collapse:collapse;
background:white;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.rehabTable th{
background:#2e7d32;
color:white;
padding:15px;
}

.rehabTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.progressStatus{
background:#fb8c00;
color:white;
padding:6px 12px;
border-radius:20px;
}

.completedStatus{
background:#2e7d32;
color:white;
padding:6px 12px;
border-radius:20px;
}

.rehabTable button{
padding:8px 14px;
margin:2px;
background:#2e7d32;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let rehabID=1;

function saveRehabRecord(){

let patient=document.getElementById("rehabPatient").value;
let condition=document.getElementById("rehabCondition").value;
let therapy=document.getElementById("therapyType").value;
let pain=document.getElementById("painScore").value;

if(patient=="" || pain==""){

alert("Please complete all required fields.");

return;

}

let status="In Progress";

if(parseInt(pain)<=2){

status="Recovered";

}

rehabID++;

let badge=(status=="Recovered")
?"<span class='completedStatus'>Recovered</span>"
:"<span class='progressStatus'>In Progress</span>";

let row="<tr>"+
"<td>"+rehabID+"</td>"+
"<td>"+patient+"</td>"+
"<td>"+condition+"</td>"+
"<td>"+therapy+"</td>"+
"<td>"+pain+"/10</td>"+
"<td>"+badge+"</td>"+
"<td><button onclick='viewRehab(this)'>View</button> <button onclick='printRehab()'>Print</button></td>"+
"</tr>";

document.getElementById("rehabBody").innerHTML+=row;

document.getElementById("rehabPatients").innerHTML=
parseInt(document.getElementById("rehabPatients").innerHTML)+1;

alert("🦴 Rehabilitation plan created successfully.");

}

function viewRehab(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+
"\nCondition : "+row.cells[2].innerHTML+
"\nTherapy : "+row.cells[3].innerHTML+
"\nPain Score : "+row.cells[4].innerHTML+
"\nStatus : "+row.cells[5].innerText

);

}

function printRehab(){

window.print();

}

</script>
<!-- ================= GENOMICS & PRECISION MEDICINE PLATFORM ================= -->

<section class="genomicsSection">

<h2 class="title">🧬 Genomics & Precision Medicine Platform</h2>

<div class="genomicsForm">

<input type="text" id="genePatient" placeholder="Patient Name">

<input type="number" id="geneAge" placeholder="Age">

<select id="geneticTest">

<option>Whole Genome Sequencing</option>
<option>Whole Exome Sequencing</option>
<option>BRCA1 / BRCA2</option>
<option>Pharmacogenomics</option>
<option>Carrier Screening</option>
<option>Cancer Gene Panel</option>
<option>Cardiac Gene Panel</option>

</select>

<select id="geneRisk">

<option>Low Risk</option>
<option>Moderate Risk</option>
<option>High Risk</option>

</select>

<input type="text" id="familyHistory" placeholder="Family Medical History">

<button onclick="saveGenomeRecord()">

🧬 Save Genome Profile

</button>

</div>

<div class="genomicsCards">

<div class="genomicsCard">

<h1 id="genomePatients">532</h1>

<p>Genome Profiles</p>

</div>

<div class="genomicsCard">

<h1 id="geneTests">1186</h1>

<p>Genetic Tests</p>

</div>

<div class="genomicsCard">

<h1 id="precisionTherapy">276</h1>

<p>Precision Treatments</p>

</div>

<div class="genomicsCard">

<h1 id="highRiskPatients">41</h1>

<p>High Risk Patients</p>

</div>

</div>

<table class="genomicsTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Genetic Test</th>

<th>Risk</th>

<th>AI Recommendation</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="genomeBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>BRCA1 / BRCA2</td>

<td>Moderate Risk</td>

<td>Annual Screening</td>

<td><span class="verified">Verified</span></td>

<td>

<button onclick="viewGenome(this)">View</button>

<button onclick="downloadGenome()">Report</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.genomicsSection{
padding:90px 8%;
background:#f7faff;
}

.genomicsForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.genomicsForm input,
.genomicsForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.genomicsForm button{
padding:15px;
background:#3949ab;
color:#fff;
border:none;
border-radius:10px;
font-weight:bold;
cursor:pointer;
}

.genomicsCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.genomicsCard{
background:#fff;
padding:30px;
border-radius:18px;
text-align:center;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.genomicsCard h1{
font-size:40px;
color:#3949ab;
}

.genomicsTable{
width:100%;
border-collapse:collapse;
background:#fff;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.genomicsTable th{
background:#3949ab;
color:#fff;
padding:15px;
}

.genomicsTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.verified{
background:#2e7d32;
color:#fff;
padding:6px 12px;
border-radius:20px;
}

.highrisk{
background:#d32f2f;
color:#fff;
padding:6px 12px;
border-radius:20px;
}

.genomicsTable button{
padding:8px 14px;
margin:2px;
background:#3949ab;
color:#fff;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let genomeID=1;

function saveGenomeRecord(){

let patient=document.getElementById("genePatient").value;
let test=document.getElementById("geneticTest").value;
let risk=document.getElementById("geneRisk").value;

if(patient==""){

alert("Please enter patient name.");

return;

}

let recommendation="Routine Follow-up";

if(risk=="Moderate Risk")
recommendation="Genetic Counseling";

if(risk=="High Risk")
recommendation="Precision Therapy & Specialist Review";

genomeID++;

let badge=(risk=="High Risk")
?"<span class='highrisk'>High Risk</span>"
:"<span class='verified'>Verified</span>";

let row="<tr>"+
"<td>"+genomeID+"</td>"+
"<td>"+patient+"</td>"+
"<td>"+test+"</td>"+
"<td>"+risk+"</td>"+
"<td>"+recommendation+"</td>"+
"<td>"+badge+"</td>"+
"<td><button onclick='viewGenome(this)'>View</button> <button onclick='downloadGenome()'>Report</button></td>"+
"</tr>";

document.getElementById("genomeBody").innerHTML+=row;

document.getElementById("genomePatients").innerHTML=
parseInt(document.getElementById("genomePatients").innerHTML)+1;

if(risk=="High Risk"){

document.getElementById("highRiskPatients").innerHTML=
parseInt(document.getElementById("highRiskPatients").innerHTML)+1;

}

alert("🧬 Genome profile saved successfully.");

}

function viewGenome(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+
"\nGenetic Test : "+row.cells[2].innerHTML+
"\nRisk : "+row.cells[3].innerHTML+
"\nRecommendation : "+row.cells[4].innerHTML

);

}

function downloadGenome(){

alert("📄 Genetic report downloaded successfully.");

}

</script>
<!-- ================= IVF & FERTILITY CENTER MANAGEMENT SYSTEM ================= -->

<section class="ivfSection">

<h2 class="title">🤰 IVF & Fertility Center Management System</h2>

<div class="ivfForm">

<input type="text" id="coupleName" placeholder="Couple Name">

<input type="number" id="femaleAge" placeholder="Female Age">

<select id="ivfCycle">

<option>Consultation</option>
<option>Ovulation Monitoring</option>
<option>Egg Retrieval</option>
<option>Fertilization</option>
<option>Embryo Transfer</option>
<option>Pregnancy Test</option>

</select>

<select id="embryoGrade">

<option>Grade A</option>
<option>Grade B</option>
<option>Grade C</option>
<option>Frozen Embryo</option>

</select>

<input type="date" id="transferDate">

<button onclick="saveIVFRecord()">

🤰 Save IVF Cycle

</button>

</div>

<div class="ivfCards">

<div class="ivfCard">

<h1 id="totalCouples">1246</h1>

<p>Registered Couples</p>

</div>

<div class="ivfCard">

<h1 id="activeCycles">215</h1>

<p>Active IVF Cycles</p>

</div>

<div class="ivfCard">

<h1 id="embryoStored">498</h1>

<p>Frozen Embryos</p>

</div>

<div class="ivfCard">

<h1 id="successRate">68%</h1>

<p>Success Rate</p>

</div>

</div>

<table class="ivfTable">

<thead>

<tr>

<th>ID</th>

<th>Couple</th>

<th>Cycle</th>

<th>Embryo</th>

<th>AI Prediction</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="ivfBody">

<tr>

<td>1</td>

<td>Rahul & Priya</td>

<td>Embryo Transfer</td>

<td>Grade A</td>

<td>High Success</td>

<td><span class="ongoing">Ongoing</span></td>

<td>

<button onclick="viewIVF(this)">View</button>

<button onclick="printIVF()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.ivfSection{
padding:90px 8%;
background:#fff8fb;
}

.ivfForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.ivfForm input,
.ivfForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.ivfForm button{
padding:15px;
background:#d81b60;
color:white;
border:none;
border-radius:10px;
font-weight:bold;
cursor:pointer;
}

.ivfCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.ivfCard{
background:white;
padding:30px;
text-align:center;
border-radius:18px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.ivfCard h1{
font-size:40px;
color:#d81b60;
}

.ivfTable{
width:100%;
border-collapse:collapse;
background:white;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.ivfTable th{
background:#d81b60;
color:white;
padding:15px;
}

.ivfTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.ongoing{
background:#fb8c00;
color:white;
padding:6px 12px;
border-radius:20px;
}

.completed{
background:#2e7d32;
color:white;
padding:6px 12px;
border-radius:20px;
}

.ivfTable button{
padding:8px 14px;
margin:2px;
background:#d81b60;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let ivfID=1;

function saveIVFRecord(){

let couple=document.getElementById("coupleName").value;
let cycle=document.getElementById("ivfCycle").value;
let embryo=document.getElementById("embryoGrade").value;

if(couple==""){

alert("Please enter couple name.");

return;

}

let prediction="Moderate Success";

if(embryo=="Grade A")
prediction="High Success";

if(embryo=="Grade C")
prediction="Low Success";

ivfID++;

let row="<tr>"+
"<td>"+ivfID+"</td>"+
"<td>"+couple+"</td>"+
"<td>"+cycle+"</td>"+
"<td>"+embryo+"</td>"+
"<td>"+prediction+"</td>"+
"<td><span class='ongoing'>Ongoing</span></td>"+
"<td><button onclick='viewIVF(this)'>View</button> <button onclick='printIVF()'>Print</button></td>"+
"</tr>";

document.getElementById("ivfBody").innerHTML+=row;

document.getElementById("totalCouples").innerHTML=
parseInt(document.getElementById("totalCouples").innerHTML)+1;

alert("🤰 IVF treatment cycle saved successfully.");

}

function viewIVF(btn){

let row=btn.parentElement.parentElement;

alert(
"Couple : "+row.cells[1].innerHTML+
"\nCycle : "+row.cells[2].innerHTML+
"\nEmbryo : "+row.cells[3].innerHTML+
"\nAI Prediction : "+row.cells[4].innerHTML+
"\nStatus : "+row.cells[5].innerText
);

}

function printIVF(){

window.print();

}

</script>
<!-- ================= ORGAN TRANSPLANT MANAGEMENT SYSTEM ================= -->

<section class="transplantSection">

<h2 class="title">🫀 Organ Transplant Management System</h2>

<div class="transplantForm">

<input type="text" id="donorName" placeholder="Donor Name">

<input type="text" id="recipientName" placeholder="Recipient Name">

<select id="organType">

<option>Kidney</option>
<option>Liver</option>
<option>Heart</option>
<option>Lung</option>
<option>Pancreas</option>
<option>Cornea</option>

</select>

<select id="bloodGroup">

<option>A+</option>
<option>A-</option>
<option>B+</option>
<option>B-</option>
<option>AB+</option>
<option>AB-</option>
<option>O+</option>
<option>O-</option>

</select>

<select id="hlaStatus">

<option>Excellent Match</option>
<option>Good Match</option>
<option>Partial Match</option>
<option>Poor Match</option>

</select>

<button onclick="registerTransplant()">

🫀 Register Transplant

</button>

</div>

<div class="transplantCards">

<div class="transplantCard">

<h1 id="donorCount">284</h1>

<p>Registered Donors</p>

</div>

<div class="transplantCard">

<h1 id="waitingPatients">152</h1>

<p>Waiting Recipients</p>

</div>

<div class="transplantCard">

<h1 id="completedTransplants">117</h1>

<p>Completed Transplants</p>

</div>

<div class="transplantCard">

<h1 id="emergencyCases">14</h1>

<p>Emergency Cases</p>

</div>

</div>

<table class="transplantTable">

<thead>

<tr>

<th>ID</th>

<th>Donor</th>

<th>Recipient</th>

<th>Organ</th>

<th>Compatibility</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="transplantBody">

<tr>

<td>1</td>

<td>Arun</td>

<td>Vijay</td>

<td>Kidney</td>

<td>Excellent Match</td>

<td><span class="approved">Approved</span></td>

<td>

<button onclick="viewTransplant(this)">View</button>

<button onclick="printTransplant()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.transplantSection{
padding:90px 8%;
background:#fff8f8;
}

.transplantForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.transplantForm input,
.transplantForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.transplantForm button{
padding:15px;
background:#c62828;
color:white;
border:none;
border-radius:10px;
font-weight:bold;
cursor:pointer;
}

.transplantCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.transplantCard{
background:white;
padding:30px;
text-align:center;
border-radius:18px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.transplantCard h1{
font-size:40px;
color:#c62828;
}

.transplantTable{
width:100%;
border-collapse:collapse;
background:white;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.transplantTable th{
background:#c62828;
color:white;
padding:15px;
}

.transplantTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.approved{
background:#2e7d32;
color:white;
padding:6px 12px;
border-radius:20px;
}

.pending{
background:#fb8c00;
color:white;
padding:6px 12px;
border-radius:20px;
}

.transplantTable button{
padding:8px 14px;
margin:2px;
background:#c62828;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let transplantID=1;

function registerTransplant(){

let donor=document.getElementById("donorName").value;
let recipient=document.getElementById("recipientName").value;
let organ=document.getElementById("organType").value;
let hla=document.getElementById("hlaStatus").value;

if(donor=="" || recipient==""){

alert("Please enter donor and recipient details.");

return;

}

let status="Pending";

if(hla=="Excellent Match"){

status="Approved";

}

transplantID++;

let badge=(status=="Approved")
?"<span class='approved'>Approved</span>"
:"<span class='pending'>Pending</span>";

let row="<tr>"+
"<td>"+transplantID+"</td>"+
"<td>"+donor+"</td>"+
"<td>"+recipient+"</td>"+
"<td>"+organ+"</td>"+
"<td>"+hla+"</td>"+
"<td>"+badge+"</td>"+
"<td><button onclick='viewTransplant(this)'>View</button> <button onclick='printTransplant()'>Print</button></td>"+
"</tr>";

document.getElementById("transplantBody").innerHTML+=row;

document.getElementById("donorCount").innerHTML=
parseInt(document.getElementById("donorCount").innerHTML)+1;

alert("🫀 Organ transplant record registered successfully.");

}

function viewTransplant(btn){

let row=btn.parentElement.parentElement;

alert(

"Donor : "+row.cells[1].innerHTML+
"\nRecipient : "+row.cells[2].innerHTML+
"\nOrgan : "+row.cells[3].innerHTML+
"\nCompatibility : "+row.cells[4].innerHTML+
"\nStatus : "+row.cells[5].innerText

);

}

function printTransplant(){

window.print();

}

</script>
<!-- ========== STEM CELL THERAPY & REGENERATIVE MEDICINE ========== -->

<section class="stemSection">

<h2 class="title">🧬 Stem Cell Therapy & Regenerative Medicine</h2>

<div class="stemForm">

<input type="text" id="donorName" placeholder="Stem Cell Donor">

<input type="text" id="patientName" placeholder="Patient Name">

<select id="stemType">

<option>Bone Marrow Stem Cell</option>
<option>Peripheral Blood Stem Cell</option>
<option>Cord Blood Stem Cell</option>
<option>Mesenchymal Stem Cell</option>
<option>Embryonic Stem Cell</option>
<option>Induced Pluripotent Stem Cell</option>

</select>

<select id="therapyType">

<option>Bone Marrow Transplant</option>
<option>Regenerative Therapy</option>
<option>Cartilage Repair</option>
<option>Neurological Therapy</option>
<option>Cardiac Regeneration</option>
<option>Diabetes Therapy</option>

</select>

<select id="cellQuality">

<option>Excellent</option>
<option>Good</option>
<option>Average</option>
<option>Poor</option>

</select>

<button onclick="saveStemCell()">

🧬 Register Therapy

</button>

</div>

<div class="stemCards">

<div class="stemCard">

<h1 id="donorTotal">468</h1>

<p>Stem Cell Donors</p>

</div>

<div class="stemCard">

<h1 id="storedCells">1324</h1>

<p>Cryogenic Samples</p>

</div>

<div class="stemCard">

<h1 id="activeTherapies">189</h1>

<p>Active Therapies</p>

</div>

<div class="stemCard">

<h1 id="successRate">94%</h1>

<p>Recovery Rate</p>

</div>

</div>

<table class="stemTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Stem Cell</th>

<th>Therapy</th>

<th>Quality</th>

<th>AI Recommendation</th>

<th>Action</th>

</tr>

</thead>

<tbody id="stemBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Bone Marrow</td>

<td>Bone Marrow Transplant</td>

<td>Excellent</td>

<td>Eligible</td>

<td>

<button onclick="viewStem(this)">View</button>

<button onclick="printStem()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.stemSection{
padding:90px 8%;
background:#f7fff9;
}

.stemForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.stemForm input,
.stemForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.stemForm button{
padding:15px;
background:#00897b;
color:white;
border:none;
border-radius:10px;
font-weight:bold;
cursor:pointer;
}

.stemCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.stemCard{
background:white;
padding:30px;
border-radius:18px;
text-align:center;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.stemCard h1{
font-size:40px;
color:#00897b;
}

.stemTable{
width:100%;
border-collapse:collapse;
background:white;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.stemTable th{
background:#00897b;
color:white;
padding:15px;
}

.stemTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.stemTable button{
padding:8px 14px;
margin:2px;
background:#00897b;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let stemID=1;

function saveStemCell(){

let donor=document.getElementById("donorName").value;

let patient=document.getElementById("patientName").value;

let stem=document.getElementById("stemType").value;

let therapy=document.getElementById("therapyType").value;

let quality=document.getElementById("cellQuality").value;

if(patient==""||donor==""){

alert("Please enter donor and patient details.");

return;

}

let ai="Needs Review";

if(quality=="Excellent") ai="Eligible";

if(quality=="Good") ai="Recommended";

if(quality=="Poor") ai="Not Recommended";

stemID++;

let row="<tr>"+

"<td>"+stemID+"</td>"+

"<td>"+patient+"</td>"+

"<td>"+stem+"</td>"+

"<td>"+therapy+"</td>"+

"<td>"+quality+"</td>"+

"<td>"+ai+"</td>"+

"<td><button onclick='viewStem(this)'>View</button> <button onclick='printStem()'>Print</button></td>"+

"</tr>";

document.getElementById("stemBody").innerHTML+=row;

document.getElementById("donorTotal").innerHTML=

parseInt(document.getElementById("donorTotal").innerHTML)+1;

alert("🧬 Stem cell therapy registered successfully.");

}

function viewStem(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+

"\nStem Cell : "+row.cells[2].innerHTML+

"\nTherapy : "+row.cells[3].innerHTML+

"\nQuality : "+row.cells[4].innerHTML+

"\nAI Recommendation : "+row.cells[5].innerHTML

);

}

function printStem(){

window.print();

}

</script>
<!-- ============== NEUROSURGERY & BRAIN MAPPING MANAGEMENT ============== -->

<section class="neuroSection">

<h2 class="title">🧠 Neurosurgery & Brain Mapping Management</h2>

<div class="neuroForm">

<input type="text" id="patientName" placeholder="Patient Name">

<input type="number" id="patientAge" placeholder="Age">

<select id="brainCondition">

<option>Brain Tumor</option>
<option>Epilepsy</option>
<option>Stroke</option>
<option>Aneurysm</option>
<option>Parkinson's Disease</option>
<option>Brain Trauma</option>
<option>Spinal Cord Injury</option>

</select>

<select id="scanType">

<option>MRI Brain</option>
<option>CT Brain</option>
<option>fMRI</option>
<option>PET Scan</option>
<option>EEG</option>
<option>MEG</option>

</select>

<select id="riskLevel">

<option>Low</option>
<option>Moderate</option>
<option>High</option>
<option>Critical</option>

</select>

<button onclick="saveNeuroCase()">

🧠 Register Case

</button>

</div>

<div class="neuroCards">

<div class="neuroCard">

<h1 id="brainCases">974</h1>

<p>Brain Cases</p>

</div>

<div class="neuroCard">

<h1 id="brainSurgeries">248</h1>

<p>Brain Surgeries</p>

</div>

<div class="neuroCard">

<h1 id="criticalPatients">39</h1>

<p>Critical Patients</p>

</div>

<div class="neuroCard">

<h1 id="mappingCases">186</h1>

<p>Brain Mapping</p>

</div>

</div>

<table class="neuroTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Diagnosis</th>

<th>Scan</th>

<th>AI Surgical Plan</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="neuroBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Brain Tumor</td>

<td>MRI Brain</td>

<td>Tumor Resection Recommended</td>

<td><span class="approved">Reviewed</span></td>

<td>

<button onclick="viewCase(this)">View</button>

<button onclick="printCase()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.neuroSection{
padding:90px 8%;
background:#f6fbff;
}

.neuroForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.neuroForm input,
.neuroForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.neuroForm button{
padding:15px;
background:#283593;
color:white;
border:none;
border-radius:10px;
cursor:pointer;
font-weight:bold;
}

.neuroCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.neuroCard{
background:white;
padding:30px;
text-align:center;
border-radius:18px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.neuroCard h1{
font-size:40px;
color:#283593;
}

.neuroTable{
width:100%;
border-collapse:collapse;
background:white;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.neuroTable th{
background:#283593;
color:white;
padding:15px;
}

.neuroTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.approved{
background:#2e7d32;
color:white;
padding:6px 12px;
border-radius:20px;
}

.critical{
background:#d32f2f;
color:white;
padding:6px 12px;
border-radius:20px;
}

.neuroTable button{
padding:8px 14px;
margin:2px;
background:#283593;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let neuroID=1;

function saveNeuroCase(){

let patient=document.getElementById("patientName").value;
let diagnosis=document.getElementById("brainCondition").value;
let scan=document.getElementById("scanType").value;
let risk=document.getElementById("riskLevel").value;

if(patient==""){

alert("Please enter patient name.");

return;

}

let aiPlan="Neurologist Review";

if(diagnosis=="Brain Tumor")
aiPlan="Tumor Resection Recommended";

if(diagnosis=="Stroke")
aiPlan="Immediate Stroke Protocol";

if(diagnosis=="Aneurysm")
aiPlan="Emergency Neurosurgery";

if(risk=="Critical"){

document.getElementById("criticalPatients").innerHTML=
parseInt(document.getElementById("criticalPatients").innerHTML)+1;

}

let badge=(risk=="Critical")
?"<span class='critical'>Critical</span>"
:"<span class='approved'>Reviewed</span>";

neuroID++;

let row="<tr>"+
"<td>"+neuroID+"</td>"+
"<td>"+patient+"</td>"+
"<td>"+diagnosis+"</td>"+
"<td>"+scan+"</td>"+
"<td>"+aiPlan+"</td>"+
"<td>"+badge+"</td>"+
"<td><button onclick='viewCase(this)'>View</button> <button onclick='printCase()'>Print</button></td>"+
"</tr>";

document.getElementById("neuroBody").innerHTML+=row;

document.getElementById("brainCases").innerHTML=
parseInt(document.getElementById("brainCases").innerHTML)+1;

alert("🧠 Neurosurgery case registered successfully.");

}

function viewCase(btn){

let row=btn.parentElement.parentElement;

alert(
"Patient : "+row.cells[1].innerHTML+
"\nDiagnosis : "+row.cells[2].innerHTML+
"\nScan : "+row.cells[3].innerHTML+
"\nAI Plan : "+row.cells[4].innerHTML+
"\nStatus : "+row.cells[5].innerText
);

}

function printCase(){

window.print();

}

</script>
<!-- ============== RADIATION ONCOLOGY MANAGEMENT SYSTEM ============== -->

<section class="radiationSection">

<h2 class="title">☢️ Radiation Oncology Management System</h2>

<div class="radiationForm">

<input type="text" id="patientName" placeholder="Patient Name">

<input type="number" id="patientAge" placeholder="Age">

<select id="cancerType">

<option>Brain Cancer</option>
<option>Breast Cancer</option>
<option>Lung Cancer</option>
<option>Prostate Cancer</option>
<option>Cervical Cancer</option>
<option>Liver Cancer</option>
<option>Head & Neck Cancer</option>

</select>

<select id="therapyType">

<option>IMRT</option>
<option>IGRT</option>
<option>VMAT</option>
<option>SBRT</option>
<option>SRS</option>
<option>3D CRT</option>

</select>

<input type="number" id="dose" placeholder="Radiation Dose (Gy)">

<button onclick="saveRadiationPlan()">

☢️ Create Treatment Plan

</button>

</div>

<div class="radiationCards">

<div class="radiationCard">

<h1 id="radiationPatients">1352</h1>

<p>Radiation Patients</p>

</div>

<div class="radiationCard">

<h1 id="linacMachines">8</h1>

<p>LINAC Machines</p>

</div>

<div class="radiationCard">

<h1 id="todaySessions">186</h1>

<p>Today's Sessions</p>

</div>

<div class="radiationCard">

<h1 id="completedFractions">19428</h1>

<p>Completed Fractions</p>

</div>

</div>

<table class="radiationTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Cancer</th>

<th>Technique</th>

<th>Dose</th>

<th>AI Planning</th>

<th>Action</th>

</tr>

</thead>

<tbody id="radiationBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Brain Cancer</td>

<td>IMRT</td>

<td>60 Gy</td>

<td>Approved</td>

<td>

<button onclick="viewRadiation(this)">View</button>

<button onclick="printRadiation()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.radiationSection{
padding:90px 8%;
background:#fffaf5;
}

.radiationForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.radiationForm input,
.radiationForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.radiationForm button{
padding:15px;
background:#ef6c00;
color:#fff;
border:none;
border-radius:10px;
font-weight:bold;
cursor:pointer;
}

.radiationCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.radiationCard{
background:#fff;
padding:30px;
text-align:center;
border-radius:18px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.radiationCard h1{
font-size:40px;
color:#ef6c00;
}

.radiationTable{
width:100%;
border-collapse:collapse;
background:#fff;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.radiationTable th{
background:#ef6c00;
color:#fff;
padding:15px;
}

.radiationTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.radiationTable button{
padding:8px 14px;
margin:2px;
background:#ef6c00;
color:#fff;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let radiationID=1;

function saveRadiationPlan(){

let patient=document.getElementById("patientName").value;
let cancer=document.getElementById("cancerType").value;
let therapy=document.getElementById("therapyType").value;
let dose=document.getElementById("dose").value;

if(patient=="" || dose==""){

alert("Please complete all fields.");

return;

}

let ai="Standard Plan";

if(therapy=="IMRT") ai="Highly Conformal Plan";
if(therapy=="VMAT") ai="Rapid Arc Optimization";
if(therapy=="SBRT") ai="High Precision Planning";

radiationID++;

let row="<tr>"+
"<td>"+radiationID+"</td>"+
"<td>"+patient+"</td>"+
"<td>"+cancer+"</td>"+
"<td>"+therapy+"</td>"+
"<td>"+dose+" Gy</td>"+
"<td>"+ai+"</td>"+
"<td><button onclick='viewRadiation(this)'>View</button> <button onclick='printRadiation()'>Print</button></td>"+
"</tr>";

document.getElementById("radiationBody").innerHTML+=row;

document.getElementById("radiationPatients").innerHTML=
parseInt(document.getElementById("radiationPatients").innerHTML)+1;

alert("☢️ Radiation treatment plan created successfully.");

}

function viewRadiation(btn){

let row=btn.parentElement.parentElement;

alert(
"Patient : "+row.cells[1].innerHTML+
"\nCancer : "+row.cells[2].innerHTML+
"\nTechnique : "+row.cells[3].innerHTML+
"\nDose : "+row.cells[4].innerHTML+
"\nAI Planning : "+row.cells[5].innerHTML
);

}

function printRadiation(){

window.print();

}

</script>
<!-- ================= NUCLEAR MEDICINE & PET-CT MANAGEMENT SYSTEM ================= -->

<section class="nuclearSection">

<h2 class="title">☢️ Nuclear Medicine & PET-CT Management System</h2>

<div class="nuclearForm">

<input type="text" id="patientName" placeholder="Patient Name">

<input type="number" id="patientAge" placeholder="Age">

<select id="scanType">

<option>PET-CT Scan</option>
<option>SPECT Scan</option>
<option>Bone Scan</option>
<option>Thyroid Scan</option>
<option>Renal Scan</option>
<option>Cardiac Perfusion Scan</option>

</select>

<select id="radioDrug">

<option>FDG (Fluorodeoxyglucose)</option>
<option>Iodine-131</option>
<option>Technetium-99m</option>
<option>Gallium-68</option>
<option>Lutetium-177</option>
<option>Fluorine-18 PSMA</option>

</select>

<input type="number" id="suvValue" placeholder="SUV Max">

<button onclick="saveNuclearCase()">

☢️ Register Scan

</button>

</div>

<div class="nuclearCards">

<div class="nuclearCard">

<h1 id="petPatients">824</h1>

<p>PET-CT Patients</p>

</div>

<div class="nuclearCard">

<h1 id="todayScans">42</h1>

<p>Today's Scans</p>

</div>

<div class="nuclearCard">

<h1 id="radioInventory">368</h1>

<p>Radioisotopes</p>

</div>

<div class="nuclearCard">

<h1 id="abnormalFindings">63</h1>

<p>Abnormal Findings</p>

</div>

</div>

<table class="nuclearTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Scan</th>

<th>Radiopharmaceutical</th>

<th>SUV</th>

<th>AI Analysis</th>

<th>Action</th>

</tr>

</thead>

<tbody id="nuclearBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>PET-CT</td>

<td>FDG</td>

<td>4.8</td>

<td>Normal Uptake</td>

<td>

<button onclick="viewScan(this)">View</button>

<button onclick="printScan()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.nuclearSection{
padding:90px 8%;
background:#fdfcff;
}

.nuclearForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.nuclearForm input,
.nuclearForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.nuclearForm button{
padding:15px;
background:#7b1fa2;
color:white;
border:none;
border-radius:10px;
font-weight:bold;
cursor:pointer;
}

.nuclearCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.nuclearCard{
background:white;
padding:30px;
text-align:center;
border-radius:18px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.nuclearCard h1{
font-size:40px;
color:#7b1fa2;
}

.nuclearTable{
width:100%;
border-collapse:collapse;
background:white;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.nuclearTable th{
background:#7b1fa2;
color:white;
padding:15px;
}

.nuclearTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.nuclearTable button{
padding:8px 14px;
margin:2px;
background:#7b1fa2;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let nuclearID=1;

function saveNuclearCase(){

let patient=document.getElementById("patientName").value;
let scan=document.getElementById("scanType").value;
let drug=document.getElementById("radioDrug").value;
let suv=document.getElementById("suvValue").value;

if(patient=="" || suv==""){

alert("Please complete all fields.");

return;

}

let ai="Normal Uptake";

if(parseFloat(suv)>=2.5)
ai="Suspicious Lesion";

if(parseFloat(suv)>=6)
ai="High Metabolic Activity";

nuclearID++;

let row="<tr>"+
"<td>"+nuclearID+"</td>"+
"<td>"+patient+"</td>"+
"<td>"+scan+"</td>"+
"<td>"+drug+"</td>"+
"<td>"+suv+"</td>"+
"<td>"+ai+"</td>"+
"<td><button onclick='viewScan(this)'>View</button> <button onclick='printScan()'>Print</button></td>"+
"</tr>";

document.getElementById("nuclearBody").innerHTML+=row;

document.getElementById("petPatients").innerHTML=
parseInt(document.getElementById("petPatients").innerHTML)+1;

if(parseFloat(suv)>=2.5){

document.getElementById("abnormalFindings").innerHTML=
parseInt(document.getElementById("abnormalFindings").innerHTML)+1;

}

alert("☢️ Nuclear medicine record added successfully.");

}

function viewScan(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+
"\nScan : "+row.cells[2].innerHTML+
"\nRadiopharmaceutical : "+row.cells[3].innerHTML+
"\nSUV Max : "+row.cells[4].innerHTML+
"\nAI Analysis : "+row.cells[5].innerHTML

);

}

function printScan(){

window.print();

}

</script>
<!-- ================= CARDIAC CATH LAB MANAGEMENT SYSTEM ================= -->

<section class="cathSection">

<h2 class="title">❤️ Cardiac Catheterization (Cath Lab) Management System</h2>

<div class="cathForm">

<input type="text" id="patientName" placeholder="Patient Name">

<input type="number" id="patientAge" placeholder="Age">

<select id="procedureType">

<option>Coronary Angiography</option>
<option>Coronary Angioplasty (PCI)</option>
<option>Primary PCI (STEMI)</option>
<option>Peripheral Angiography</option>
<option>Pacemaker Implantation</option>
<option>Cardiac Catheterization</option>

</select>

<select id="arteryStatus">

<option>Normal</option>
<option>30% Blockage</option>
<option>50% Blockage</option>
<option>70% Blockage</option>
<option>90% Blockage</option>
<option>100% Occlusion</option>

</select>

<input type="number" id="stentCount" placeholder="Number of Stents">

<button onclick="saveCathProcedure()">

❤️ Register Procedure

</button>

</div>

<div class="cathCards">

<div class="cathCard">

<h1 id="cathPatients">1684</h1>

<p>Cath Lab Patients</p>

</div>

<div class="cathCard">

<h1 id="angioplastyCount">652</h1>

<p>Angioplasties</p>

</div>

<div class="cathCard">

<h1 id="emergencyPCI">104</h1>

<p>Emergency PCI</p>

</div>

<div class="cathCard">

<h1 id="stentInventory">428</h1>

<p>Available Stents</p>

</div>

</div>

<table class="cathTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Procedure</th>

<th>Blockage</th>

<th>AI Assessment</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="cathBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Coronary Angioplasty</td>

<td>90% Blockage</td>

<td>Urgent PCI Recommended</td>

<td><span class="completed">Completed</span></td>

<td>

<button onclick="viewCath(this)">View</button>

<button onclick="printCath()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.cathSection{
padding:90px 8%;
background:#fff5f5;
}

.cathForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.cathForm input,
.cathForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.cathForm button{
padding:15px;
background:#c62828;
color:white;
border:none;
border-radius:10px;
font-weight:bold;
cursor:pointer;
}

.cathCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.cathCard{
background:white;
padding:30px;
text-align:center;
border-radius:18px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.cathCard h1{
font-size:40px;
color:#c62828;
}

.cathTable{
width:100%;
border-collapse:collapse;
background:white;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.cathTable th{
background:#c62828;
color:white;
padding:15px;
}

.cathTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.completed{
background:#2e7d32;
color:white;
padding:6px 12px;
border-radius:20px;
}

.pending{
background:#ef6c00;
color:white;
padding:6px 12px;
border-radius:20px;
}

.cathTable button{
padding:8px 14px;
margin:2px;
background:#c62828;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let cathID=1;

function saveCathProcedure(){

let patient=document.getElementById("patientName").value;

let procedure=document.getElementById("procedureType").value;

let blockage=document.getElementById("arteryStatus").value;

let stents=parseInt(document.getElementById("stentCount").value)||0;

if(patient==""){

alert("Please enter patient details.");

return;

}

let ai="Routine Follow-up";

if(blockage=="70% Blockage")
ai="Angioplasty Recommended";

if(blockage=="90% Blockage")
ai="Urgent PCI Required";

if(blockage=="100% Occlusion")
ai="Emergency STEMI Protocol";

if(stents>0){

document.getElementById("stentInventory").innerHTML=
parseInt(document.getElementById("stentInventory").innerHTML)-stents;

}

if(procedure=="Primary PCI (STEMI)"){

document.getElementById("emergencyPCI").innerHTML=
parseInt(document.getElementById("emergencyPCI").innerHTML)+1;

}

cathID++;

let row="<tr>"+
"<td>"+cathID+"</td>"+
"<td>"+patient+"</td>"+
"<td>"+procedure+"</td>"+
"<td>"+blockage+"</td>"+
"<td>"+ai+"</td>"+
"<td><span class='pending'>Scheduled</span></td>"+
"<td><button onclick='viewCath(this)'>View</button> <button onclick='printCath()'>Print</button></td>"+
"</tr>";

document.getElementById("cathBody").innerHTML+=row;

document.getElementById("cathPatients").innerHTML=
parseInt(document.getElementById("cathPatients").innerHTML)+1;

alert("❤️ Cath Lab procedure registered successfully.");

}

function viewCath(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+
"\nProcedure : "+row.cells[2].innerHTML+
"\nCoronary Status : "+row.cells[3].innerHTML+
"\nAI Assessment : "+row.cells[4].innerHTML+
"\nStatus : "+row.cells[5].innerText

);

}

function printCath(){

window.print();

}

</script>
<!-- ================= PULMONOLOGY & BRONCHOSCOPY MANAGEMENT SYSTEM ================= -->

<section class="pulmoSection">

<h2 class="title">🫁 Pulmonology & Bronchoscopy Management System</h2>

<div class="pulmoForm">

<input type="text" id="patientName" placeholder="Patient Name">

<input type="number" id="patientAge" placeholder="Age">

<select id="lungDisease">

<option>Asthma</option>
<option>COPD</option>
<option>Pneumonia</option>
<option>Tuberculosis</option>
<option>Lung Cancer</option>
<option>Interstitial Lung Disease</option>
<option>Sleep Apnea</option>

</select>

<select id="procedure">

<option>Pulmonary Function Test (PFT)</option>
<option>Bronchoscopy</option>
<option>BAL Procedure</option>
<option>EBUS</option>
<option>Sleep Study</option>
<option>Ventilator Assessment</option>

</select>

<select id="severity">

<option>Mild</option>
<option>Moderate</option>
<option>Severe</option>
<option>Critical</option>

</select>

<button onclick="savePulmoRecord()">

🫁 Register Patient

</button>

</div>

<div class="pulmoCards">

<div class="pulmoCard">

<h1 id="pulmoPatients">2456</h1>

<p>Pulmonology Patients</p>

</div>

<div class="pulmoCard">

<h1 id="bronchoscopyCases">386</h1>

<p>Bronchoscopies</p>

</div>

<div class="pulmoCard">

<h1 id="ventilatorCases">74</h1>

<p>Ventilator Patients</p>

</div>

<div class="pulmoCard">

<h1 id="criticalLungs">29</h1>

<p>Critical Cases</p>

</div>

</div>

<table class="pulmoTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Disease</th>

<th>Procedure</th>

<th>AI Recommendation</th>

<th>Status</th>

<th>Action</th>

</tr>

</thead>

<tbody id="pulmoBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>COPD</td>

<td>PFT</td>

<td>Bronchodilator Therapy</td>

<td><span class="completed">Reviewed</span></td>

<td>

<button onclick="viewPulmo(this)">View</button>

<button onclick="printPulmo()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.pulmoSection{
padding:90px 8%;
background:#f5fcff;
}

.pulmoForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.pulmoForm input,
.pulmoForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.pulmoForm button{
padding:15px;
background:#00838f;
color:white;
border:none;
border-radius:10px;
font-weight:bold;
cursor:pointer;
}

.pulmoCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.pulmoCard{
background:white;
padding:30px;
text-align:center;
border-radius:18px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.pulmoCard h1{
font-size:40px;
color:#00838f;
}

.pulmoTable{
width:100%;
border-collapse:collapse;
background:white;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.pulmoTable th{
background:#00838f;
color:white;
padding:15px;
}

.pulmoTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.completed{
background:#2e7d32;
color:white;
padding:6px 12px;
border-radius:20px;
}

.critical{
background:#c62828;
color:white;
padding:6px 12px;
border-radius:20px;
}

.pulmoTable button{
padding:8px 14px;
margin:2px;
background:#00838f;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let pulmoID=1;

function savePulmoRecord(){

let patient=document.getElementById("patientName").value;

let disease=document.getElementById("lungDisease").value;

let procedure=document.getElementById("procedure").value;

let severity=document.getElementById("severity").value;

if(patient==""){

alert("Please enter patient name.");

return;

}

let ai="Routine Pulmonary Care";

if(disease=="COPD") ai="Bronchodilator Therapy";

if(disease=="Asthma") ai="Inhaler Optimization";

if(disease=="Tuberculosis") ai="Start Anti-TB Protocol";

if(disease=="Lung Cancer") ai="Oncology Referral";

if(severity=="Critical"){

ai="Immediate ICU Admission";

document.getElementById("criticalLungs").innerHTML=
parseInt(document.getElementById("criticalLungs").innerHTML)+1;

}

if(procedure=="Bronchoscopy"){

document.getElementById("bronchoscopyCases").innerHTML=
parseInt(document.getElementById("bronchoscopyCases").innerHTML)+1;

}

if(procedure=="Ventilator Assessment"){

document.getElementById("ventilatorCases").innerHTML=
parseInt(document.getElementById("ventilatorCases").innerHTML)+1;

}

pulmoID++;

let badge=(severity=="Critical")
?"<span class='critical'>Critical</span>"
:"<span class='completed'>Reviewed</span>";

let row="<tr>"+
"<td>"+pulmoID+"</td>"+
"<td>"+patient+"</td>"+
"<td>"+disease+"</td>"+
"<td>"+procedure+"</td>"+
"<td>"+ai+"</td>"+
"<td>"+badge+"</td>"+
"<td><button onclick='viewPulmo(this)'>View</button> <button onclick='printPulmo()'>Print</button></td>"+
"</tr>";

document.getElementById("pulmoBody").innerHTML+=row;

document.getElementById("pulmoPatients").innerHTML=
parseInt(document.getElementById("pulmoPatients").innerHTML)+1;

alert("🫁 Pulmonology record created successfully.");

}

function viewPulmo(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+

"\nDisease : "+row.cells[2].innerHTML+

"\nProcedure : "+row.cells[3].innerHTML+

"\nAI Recommendation : "+row.cells[4].innerHTML+

"\nStatus : "+row.cells[5].innerText

);

}

function printPulmo(){

window.print();

}

</script>
<!-- ================= HEMATOLOGY & BONE MARROW TRANSPLANT MANAGEMENT SYSTEM ================= -->

<section class="hemaSection">

<h2 class="title">🩸 Hematology & Bone Marrow Transplant Management</h2>

<div class="hemaForm">

<input type="text" id="patientName" placeholder="Patient Name">

<input type="number" id="patientAge" placeholder="Age">

<select id="bloodDisease">

<option>Leukemia</option>
<option>Lymphoma</option>
<option>Multiple Myeloma</option>
<option>Aplastic Anemia</option>
<option>Thalassemia</option>
<option>Sickle Cell Disease</option>
<option>Hemophilia</option>

</select>

<select id="transplantType">

<option>Autologous BMT</option>
<option>Allogeneic BMT</option>
<option>Cord Blood Transplant</option>
<option>Stem Cell Rescue</option>
<option>Chemotherapy</option>

</select>

<select id="donorMatch">

<option>100% Match</option>
<option>90% Match</option>
<option>80% Match</option>
<option>Partial Match</option>

</select>

<button onclick="saveBMTRecord()">

🩸 Register BMT Case

</button>

</div>

<div class="hemaCards">

<div class="hemaCard">

<h1 id="hemaPatients">1268</h1>

<p>Hematology Patients</p>

</div>

<div class="hemaCard">

<h1 id="bmtCases">214</h1>

<p>BMT Procedures</p>

</div>

<div class="hemaCard">

<h1 id="donorRegistry">862</h1>

<p>Donor Registry</p>

</div>

<div class="hemaCard">

<h1 id="criticalCases">47</h1>

<p>Critical Cases</p>

</div>

</div>

<table class="hemaTable">

<thead>

<tr>

<th>ID</th>

<th>Patient</th>

<th>Disease</th>

<th>Procedure</th>

<th>Donor Match</th>

<th>AI Recommendation</th>

<th>Action</th>

</tr>

</thead>

<tbody id="hemaBody">

<tr>

<td>1</td>

<td>Rahul</td>

<td>Leukemia</td>

<td>Allogeneic BMT</td>

<td>100%</td>

<td>Proceed with Transplant</td>

<td>

<button onclick="viewBMT(this)">View</button>

<button onclick="printBMT()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.hemaSection{
padding:90px 8%;
background:#fff8f8;
}

.hemaForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:30px;
}

.hemaForm input,
.hemaForm select{
padding:15px;
border:1px solid #ccc;
border-radius:10px;
}

.hemaForm button{
padding:15px;
background:#b71c1c;
color:white;
border:none;
border-radius:10px;
font-weight:bold;
cursor:pointer;
}

.hemaCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:20px;
margin-bottom:30px;
}

.hemaCard{
background:white;
padding:30px;
text-align:center;
border-radius:18px;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.hemaCard h1{
font-size:40px;
color:#b71c1c;
}

.hemaTable{
width:100%;
border-collapse:collapse;
background:white;
border-radius:15px;
overflow:hidden;
box-shadow:0 10px 20px rgba(0,0,0,.08);
}

.hemaTable th{
background:#b71c1c;
color:white;
padding:15px;
}

.hemaTable td{
padding:15px;
text-align:center;
border-bottom:1px solid #eee;
}

.hemaTable button{
padding:8px 14px;
margin:2px;
background:#b71c1c;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let hemaID=1;

function saveBMTRecord(){

let patient=document.getElementById("patientName").value;
let disease=document.getElementById("bloodDisease").value;
let procedure=document.getElementById("transplantType").value;
let match=document.getElementById("donorMatch").value;

if(patient==""){

alert("Please enter patient name.");

return;

}

let ai="Further Evaluation";

if(match=="100% Match") ai="Proceed with Transplant";
if(match=="90% Match") ai="Eligible with Monitoring";
if(match=="80% Match") ai="Additional Compatibility Testing";
if(match=="Partial Match") ai="Search Alternative Donor";

hemaID++;

let row="<tr>"+
"<td>"+hemaID+"</td>"+
"<td>"+patient+"</td>"+
"<td>"+disease+"</td>"+
"<td>"+procedure+"</td>"+
"<td>"+match+"</td>"+
"<td>"+ai+"</td>"+
"<td><button onclick='viewBMT(this)'>View</button> <button onclick='printBMT()'>Print</button></td>"+
"</tr>";

document.getElementById("hemaBody").innerHTML+=row;

document.getElementById("hemaPatients").innerHTML=
parseInt(document.getElementById("hemaPatients").innerHTML)+1;

if(procedure.includes("BMT")){

document.getElementById("bmtCases").innerHTML=
parseInt(document.getElementById("bmtCases").innerHTML)+1;

}

alert("🩸 Hematology/BMT record created successfully.");

}

function viewBMT(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+
"\nDisease : "+row.cells[2].innerHTML+
"\nProcedure : "+row.cells[3].innerHTML+
"\nDonor Match : "+row.cells[4].innerHTML+
"\nAI Recommendation : "+row.cells[5].innerHTML

);

}

function printBMT(){

window.print();

}

</script>
<!-- ================= NICU MANAGEMENT SYSTEM ================= -->

<section class="nicuSection">

<h2 class="title">👶 NICU Management System</h2>

<div class="nicuForm">

<input type="text" id="babyName" placeholder="Baby Name">

<input type="text" id="motherName" placeholder="Mother Name">

<input type="number" id="babyWeight" placeholder="Weight (kg)">

<select id="nicuCondition">
<option>Premature Baby</option>
<option>Low Birth Weight</option>
<option>Respiratory Distress</option>
<option>Jaundice</option>
<option>Sepsis</option>
<option>Congenital Disorder</option>
</select>

<select id="nicuBed">
<option>Incubator-01</option>
<option>Incubator-02</option>
<option>NICU Bed-03</option>
<option>NICU Bed-04</option>
</select>

<button onclick="saveNICU()">👶 Admit Baby</button>

</div>

<div class="nicuCards">

<div class="nicuCard">
<h1 id="nicuPatients">142</h1>
<p>NICU Babies</p>
</div>

<div class="nicuCard">
<h1 id="nicuIncubators">28</h1>
<p>Incubators Active</p>
</div>

<div class="nicuCard">
<h1 id="nicuCritical">9</h1>
<p>Critical Babies</p>
</div>

<div class="nicuCard">
<h1 id="nicuDischarge">118</h1>
<p>Discharged</p>
</div>

</div>

<table class="nicuTable">

<thead>

<tr>

<th>ID</th>
<th>Baby</th>
<th>Mother</th>
<th>Weight</th>
<th>Condition</th>
<th>AI Risk</th>
<th>Bed</th>
<th>Action</th>

</tr>

</thead>

<tbody id="nicuBody">

<tr>

<td>1</td>
<td>Baby Rahul</td>
<td>Priya</td>
<td>2.5 Kg</td>
<td>Premature</td>
<td>Medium</td>
<td>Incubator-01</td>

<td>

<button onclick="viewNICU(this)">View</button>

<button onclick="printNICU()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.nicuSection{
padding:80px 8%;
background:#eef9ff;
}

.nicuForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:25px;
}

.nicuForm input,
.nicuForm select{
padding:14px;
border-radius:10px;
border:1px solid #ccc;
}

.nicuForm button{
background:#00acc1;
color:white;
border:none;
padding:14px;
border-radius:10px;
cursor:pointer;
font-weight:bold;
}

.nicuCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
gap:20px;
margin-bottom:25px;
}

.nicuCard{
background:white;
padding:25px;
text-align:center;
border-radius:15px;
box-shadow:0 8px 18px rgba(0,0,0,.08);
}

.nicuCard h1{
font-size:38px;
color:#00acc1;
}

.nicuTable{
width:100%;
background:white;
border-collapse:collapse;
border-radius:15px;
overflow:hidden;
}

.nicuTable th{
background:#00acc1;
color:white;
padding:14px;
}

.nicuTable td{
padding:14px;
text-align:center;
border-bottom:1px solid #eee;
}

.nicuTable button{
padding:8px 12px;
border:none;
background:#00acc1;
color:white;
border-radius:8px;
cursor:pointer;
margin:2px;
}

</style>

<script>

let nicuID=1;

function saveNICU(){

let baby=document.getElementById("babyName").value;

let mother=document.getElementById("motherName").value;

let weight=document.getElementById("babyWeight").value;

let condition=document.getElementById("nicuCondition").value;

let bed=document.getElementById("nicuBed").value;

if(baby=="" || mother==""){

alert("Enter Baby Details");

return;

}

let risk="Low";

if(weight<2.5) risk="Medium";

if(weight<1.5) risk="High";

nicuID++;

let row="<tr>"+
"<td>"+nicuID+"</td>"+
"<td>"+baby+"</td>"+
"<td>"+mother+"</td>"+
"<td>"+weight+" Kg</td>"+
"<td>"+condition+"</td>"+
"<td>"+risk+"</td>"+
"<td>"+bed+"</td>"+
"<td><button onclick='viewNICU(this)'>View</button> <button onclick='printNICU()'>Print</button></td>"+
"</tr>";

document.getElementById("nicuBody").innerHTML+=row;

document.getElementById("nicuPatients").innerHTML=
parseInt(document.getElementById("nicuPatients").innerHTML)+1;

if(risk=="High"){

document.getElementById("nicuCritical").innerHTML=
parseInt(document.getElementById("nicuCritical").innerHTML)+1;

}

alert("👶 Baby admitted successfully.");

}

function viewNICU(btn){

let row=btn.parentElement.parentElement;

alert(
"Baby : "+row.cells[1].innerHTML+
"\nMother : "+row.cells[2].innerHTML+
"\nWeight : "+row.cells[3].innerHTML+
"\nCondition : "+row.cells[4].innerHTML+
"\nAI Risk : "+row.cells[5].innerHTML+
"\nBed : "+row.cells[6].innerHTML
);

}

function printNICU(){

window.print();

}

</script>
<!-- ================= PEDIATRICS MANAGEMENT SYSTEM ================= -->

<section class="pediatricSection">

<h2 class="title">👧 Pediatrics Management System</h2>

<div class="pediatricForm">

<input type="text" id="childName" placeholder="Child Name">

<input type="text" id="parentName" placeholder="Parent / Guardian">

<input type="number" id="childAge" placeholder="Age (Years)">

<input type="number" id="childWeight" placeholder="Weight (Kg)">

<select id="bloodGroup">

<option>A+</option>
<option>A-</option>
<option>B+</option>
<option>B-</option>
<option>AB+</option>
<option>AB-</option>
<option>O+</option>
<option>O-</option>

</select>

<select id="disease">

<option>Fever</option>
<option>Cold & Cough</option>
<option>Asthma</option>
<option>Diarrhea</option>
<option>Typhoid</option>
<option>Dengue</option>
<option>Chickenpox</option>
<option>Routine Checkup</option>

</select>

<button onclick="saveChild()">

👧 Register Child

</button>

</div>

<div class="pediatricCards">

<div class="pediatricCard">

<h1 id="totalChildren">652</h1>

<p>Registered Children</p>

</div>

<div class="pediatricCard">

<h1 id="todayVisit">38</h1>

<p>Today's Visits</p>

</div>

<div class="pediatricCard">

<h1 id="vaccinationPending">26</h1>

<p>Vaccination Pending</p>

</div>

<div class="pediatricCard">

<h1 id="criticalChildren">5</h1>

<p>Critical Cases</p>

</div>

</div>

<table class="pediatricTable">

<thead>

<tr>

<th>ID</th>
<th>Child</th>
<th>Parent</th>
<th>Age</th>
<th>Disease</th>
<th>AI Advice</th>
<th>Action</th>

</tr>

</thead>

<tbody id="childBody">

<tr>

<td>1</td>
<td>Arjun</td>
<td>Ravi</td>
<td>5</td>
<td>Fever</td>
<td>Paracetamol & Hydration</td>

<td>

<button onclick="viewChild(this)">View</button>

<button onclick="printChild()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.pediatricSection{
padding:80px 8%;
background:#fffdf5;
}

.pediatricForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:25px;
}

.pediatricForm input,
.pediatricForm select{
padding:14px;
border-radius:10px;
border:1px solid #ccc;
}

.pediatricForm button{
background:#43a047;
color:white;
border:none;
padding:14px;
border-radius:10px;
font-weight:bold;
cursor:pointer;
}

.pediatricCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
gap:20px;
margin-bottom:25px;
}

.pediatricCard{
background:white;
padding:25px;
border-radius:15px;
text-align:center;
box-shadow:0 8px 18px rgba(0,0,0,.08);
}

.pediatricCard h1{
font-size:38px;
color:#43a047;
}

.pediatricTable{
width:100%;
background:white;
border-collapse:collapse;
border-radius:15px;
overflow:hidden;
}

.pediatricTable th{
background:#43a047;
color:white;
padding:14px;
}

.pediatricTable td{
padding:14px;
text-align:center;
border-bottom:1px solid #eee;
}

.pediatricTable button{
padding:8px 12px;
margin:2px;
background:#43a047;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let childID=1;

function saveChild(){

let child=document.getElementById("childName").value;

let parent=document.getElementById("parentName").value;

let age=parseInt(document.getElementById("childAge").value);

let disease=document.getElementById("disease").value;

if(child=="" || parent==""){

alert("Please enter child details.");

return;

}

let ai="Routine Checkup";

if(disease=="Fever")
ai="Paracetamol & Hydration";

if(disease=="Asthma")
ai="Nebulization Recommended";

if(disease=="Dengue")
ai="Platelet Monitoring";

if(disease=="Typhoid")
ai="Antibiotic Therapy";

if(age<1)
ai="Neonatal/Pediatric Specialist Review";

childID++;

let row="<tr>"+
"<td>"+childID+"</td>"+
"<td>"+child+"</td>"+
"<td>"+parent+"</td>"+
"<td>"+age+"</td>"+
"<td>"+disease+"</td>"+
"<td>"+ai+"</td>"+
"<td><button onclick='viewChild(this)'>View</button> <button onclick='printChild()'>Print</button></td>"+
"</tr>";

document.getElementById("childBody").innerHTML+=row;

document.getElementById("totalChildren").innerHTML=
parseInt(document.getElementById("totalChildren").innerHTML)+1;

if(disease=="Dengue"){

document.getElementById("criticalChildren").innerHTML=
parseInt(document.getElementById("criticalChildren").innerHTML)+1;

}

alert("👧 Child registered successfully.");

}

function viewChild(btn){

let row=btn.parentElement.parentElement;

alert(

"Child : "+row.cells[1].innerHTML+
"\nParent : "+row.cells[2].innerHTML+
"\nAge : "+row.cells[3].innerHTML+
"\nDisease : "+row.cells[4].innerHTML+
"\nAI Advice : "+row.cells[5].innerHTML

);

}

function printChild(){

window.print();

}

</script>
<!-- ================= GERIATRIC CARE MANAGEMENT SYSTEM ================= -->

<section class="geriatricSection">

<h2 class="title">👴 Geriatric Care Management System</h2>

<div class="geriatricForm">

<input type="text" id="patientName" placeholder="Patient Name">

<input type="number" id="patientAge" placeholder="Age">

<select id="gender">
<option>Male</option>
<option>Female</option>
<option>Other</option>
</select>

<select id="disease">

<option>Hypertension</option>
<option>Diabetes</option>
<option>Heart Disease</option>
<option>Arthritis</option>
<option>Parkinson's Disease</option>
<option>Alzheimer's Disease</option>
<option>Stroke Follow-up</option>
<option>Routine Check-up</option>

</select>

<select id="mobility">

<option>Independent</option>
<option>Walking Stick</option>
<option>Walker</option>
<option>Wheelchair</option>
<option>Bedridden</option>

</select>

<button onclick="saveSenior()">

👴 Register Patient

</button>

</div>

<div class="geriatricCards">

<div class="geriatricCard">
<h1 id="seniorPatients">528</h1>
<p>Senior Patients</p>
</div>

<div class="geriatricCard">
<h1 id="routineVisit">36</h1>
<p>Today's Visits</p>
</div>

<div class="geriatricCard">
<h1 id="highRisk">18</h1>
<p>High Risk</p>
</div>

<div class="geriatricCard">
<h1 id="homeCare">44</h1>
<p>Home Care</p>
</div>

</div>

<table class="geriatricTable">

<thead>

<tr>

<th>ID</th>
<th>Patient</th>
<th>Age</th>
<th>Disease</th>
<th>Mobility</th>
<th>AI Advice</th>
<th>Action</th>

</tr>

</thead>

<tbody id="geriatricBody">

<tr>

<td>1</td>
<td>Raman</td>
<td>72</td>
<td>Hypertension</td>
<td>Walking Stick</td>
<td>Monthly BP Monitoring</td>

<td>

<button onclick="viewSenior(this)">View</button>

<button onclick="printSenior()">Print</button>

</td>

</tr>

</tbody>

</table>

</section>

<style>

.geriatricSection{
padding:80px 8%;
background:#f9f9f9;
}

.geriatricForm{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
margin-bottom:25px;
}

.geriatricForm input,
.geriatricForm select{
padding:14px;
border-radius:10px;
border:1px solid #ccc;
}

.geriatricForm button{
background:#6d4c41;
color:white;
border:none;
padding:14px;
border-radius:10px;
font-weight:bold;
cursor:pointer;
}

.geriatricCards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
gap:20px;
margin-bottom:25px;
}

.geriatricCard{
background:white;
padding:25px;
border-radius:15px;
text-align:center;
box-shadow:0 8px 18px rgba(0,0,0,.08);
}

.geriatricCard h1{
font-size:38px;
color:#6d4c41;
}

.geriatricTable{
width:100%;
background:white;
border-collapse:collapse;
border-radius:15px;
overflow:hidden;
}

.geriatricTable th{
background:#6d4c41;
color:white;
padding:14px;
}

.geriatricTable td{
padding:14px;
text-align:center;
border-bottom:1px solid #eee;
}

.geriatricTable button{
padding:8px 12px;
margin:2px;
background:#6d4c41;
color:white;
border:none;
border-radius:8px;
cursor:pointer;
}

</style>

<script>

let seniorID=1;

function saveSenior(){

let patient=document.getElementById("patientName").value;

let age=parseInt(document.getElementById("patientAge").value);

let disease=document.getElementById("disease").value;

let mobility=document.getElementById("mobility").value;

if(patient==""){

alert("Please enter patient details.");

return;

}

let ai="Routine Health Check";

if(disease=="Diabetes")
ai="HbA1c Every 3 Months";

if(disease=="Hypertension")
ai="Monthly BP Monitoring";

if(disease=="Heart Disease")
ai="ECG & Cardiology Review";

if(disease=="Alzheimer's Disease")
ai="Memory Clinic Follow-up";

if(mobility=="Wheelchair")
ai="Physiotherapy + Fall Prevention";

if(mobility=="Bedridden")
ai="Home Nursing Recommended";

seniorID++;

let row="<tr>"+
"<td>"+seniorID+"</td>"+
"<td>"+patient+"</td>"+
"<td>"+age+"</td>"+
"<td>"+disease+"</td>"+
"<td>"+mobility+"</td>"+
"<td>"+ai+"</td>"+
"<td><button onclick='viewSenior(this)'>View</button> <button onclick='printSenior()'>Print</button></td>"+
"</tr>";

document.getElementById("geriatricBody").innerHTML+=row;

document.getElementById("seniorPatients").innerHTML=
parseInt(document.getElementById("seniorPatients").innerHTML)+1;

if(age>=80){

document.getElementById("highRisk").innerHTML=
parseInt(document.getElementById("highRisk").innerHTML)+1;

}

alert("👴 Senior patient registered successfully.");

}

function viewSenior(btn){

let row=btn.parentElement.parentElement;

alert(

"Patient : "+row.cells[1].innerHTML+
"\nAge : "+row.cells[2].innerHTML+
"\nDisease : "+row.cells[3].innerHTML+
"\nMobility : "+row.cells[4].innerHTML+
"\nAI Advice : "+row.cells[5].innerHTML

);

}

function printSenior(){

window.print();

}

</script>










