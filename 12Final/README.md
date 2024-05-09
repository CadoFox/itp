# Final Project - "CadoFox.com" Portfolio Website

## Approach: Heavily modifying template
### I should first mention that for this project, I chose to browse the website provided for a template that matched what I was after as closely as possible

I settled on [this one](https://html5up.net/uploads/demos/big-picture/), which actually put me quite ahead as it was pretty damn close to what I wanted

# Header

## Goal: Transparent statiic floating header with logo

This was actually an element I wanted to carry over from my last attempt to use an "all in one editor" to make my website. I like the idea of simplicity and letting the content do the work, much like the inspirations I drew from, so I like the idea of the buttons and icon just floating over top everything out of the way

This was mainly just a matter of changing opacity and positioning of the original header, such that the header stays visible, but with a transparent background, and ALSO does not affect the positioning of the first section.

			<header id="header">
				<a href="https://cadofox.com">
					<img class="logo" id="headerlogo" src="/images/Logos/CF_Text_W_small.png" alt="CadoFox logo">
				</a>
				
				<nav>
					<ul>
						<li><a href="#intro">HOME</a></li>
						<li><a href="#one">ABOUT</a></li>
						<li><a href="#two">SERVICES</a></li>
						<li><a href="#work">WORKS</a></li>
						<li><a href="#contact">CONTACT</a></li>
					</ul>
				</nav>
			</header>

# The corresponding CSS:

                    #header {
            position: fixed;
            z-index: 10000;
            left: 0;
            top: 0;
            width: 100%;
            background: rgba(0, 0, 0, 0);
            height: 3em;
            line-height: 3em;
            /* box-shadow: 0 0 0.15em 0 rgba(0, 0, 0, 0); */
         }

I switched the position declaration to "fixed", and used VS codes color picker to set the alpha all the way transparent

# Sections

## Goal: I initially just wanted a nice landing page with my logo really big, an about section, a services section, and a works section. Then I saw that the template had pretty much all this PLUS a contact form (more on that later)

## Then later I decided I also wanted to take inspirationg from my good friend CBU3D, [whos website i really like](cbu3d.com). (Also more on this later)

Heres a stripped down just basic structure of what I ended up with, broken up with my thoughts

            <!-- Intro -->
			<section id="intro" class="main style1 dark fullscreen">
				<div class="content">
					<!-- Intro Logo -->
					<!-- <div id="biglogo" class="content"> -->
						<header>

						</header>
							<!-- <h2>CadoFox</h2> -->
							<div>
								<img class="logo headerlogo" src="/images/Logos/CF_Text_W_medium.png" alt="CadoFox logo">
							</div>						
							<p id="introsubtitle"> MUSIC • DESIGN • VISUALS</p>
						<footer>
							<a href="#one" class="button style2 down">More</a>
						</footer>
					<!-- </div> -->
				</div>
			</section>

Logo proved a tiny bit difficult, as I had to figure out how to properly size it. Ultimately, I created a custom class and id for it, which actaully made things quite simple, as opposed to trying to use the existing elements of the template

		<!-- Showcase -->
		<section class="showcase">
			<div class="showcase-div" style="--video-index: 0;">
			  <div class="showcase-container">
				<video class="showcase-videosrc" playsinline preload="auto" muted loop autoplay src="/videos/CF_FlyinAround-720.mp4" type="video/mp4">
				  your browser does not support the video tag

This was probably the most difficult and the biggest "fail" of this website's design. More on this below.

		<!-- About -->
			<section id="one" class="main style2 right dark fullscreen">
				<div class="bgvideocontainer">
					<video class="bgvideosrc" playsinline preload="auto" muted loop autoplay src="/videos/CF_Website_LiveVideos.mp4" type="video/mp4">
						your browser does not support the video tag
					  </video>
				</div>
				<div class="content box style2">
					<header>
						<h2>ABOUT</h2>
					</header>
					<p>Southern Cali born audio-visual artist, under the alias “CadoFox”. I make music, graphic design, and visuals</p>
				</div>
				<a href="#two" class="button style2 down anchored">Next</a>
			</section>

		<!-- Services -->
			<section id="two" class="main style2 left dark fullscreen">
				<div class="bgvideocontainer">
					<video class="bgvideosrc" playsinline preload="auto" muted loop autoplay src="/videos/CF_Website_VisualsReel.mp4" type="video/mp4">
						your browser does not support the video tag
					  </video>
				</div>
				
				<div class="content box style2">
					<header>
						<h2>SERVICES</h2>
					</header>
					<p>Graphic Design: Logos/Custom Typography, Cover art, posters, socials banners, etc.</p>
					<p>Visuals: DJ/Projection visuals, release teasers, music videos, abstract 3D, visualizers</p>
				</div>
				<a href="#work" class="button style2 down anchored">Next</a>
			</section>

Quite straight forward, although it took me a good 30 minutes to figure out where to put the video for the background and how to have it FUNCTION as the background, without getting in the way of the text boxes (thank you display: flex !!)


		<!-- Work -->
			<section id="work" class="main style3 primary">
				<div class="content">
					<header>
						<h2>WORKS</h2>
						
					</header>

					<!-- Gallery  -->
						<div class="gallery">
							<article class="from-left">
								<div class="gallerycontainer">
									<div class="galleryvideo">
										<video class="galleryvideosrc" playsinline preload="auto" muted loop autoplay src="/videos/CF_FlyinAround-720.mp4" type="video/mp4">
											your browser does not support the video tag
										  
This was also fairly straight forward. My battle with the showcase section left me well prepared for handling replacing the images with autoplaying videos. I had a bit of a problem with the sizing at first, but remembering what I was learning from the showcase section offered the best solution: Just Put It In More Divs. This seems to be a running tactic of mine haha


		<!-- Contact -->
			<section id="contact" class="main style3 secondary">
				<div class="content">
					<!-- <header>
						<h2>CONTTACT</h2>
						<p>Commissions: OPEN - 2 SLOTS</p>
					</header> -->
					<div class="box">
						<h1>
							<a href="mailto:contact@cadofox.com" style="font-size: 3em;">contact@cadofox.com</a>
							
						</h1>
						<p>Commissions: OPEN - 2 SLOTS</p>
					</div>
				</div>
			</section>

Originally, this section had a FORM in the template. I was later made aware that unfortunately there is no way to make forms work on github websites. Thankfully, I already had a piece of knowledge from my first attempt at a website, which was to use the mailto:xyz link!

Removing the form and replacing it with my contact email in big letters as a functional link that auto opens and creates an email addressed to me, ready for the use to type in and send off, was pretty straight forward. 

# The Showcase Section Battle of Spring 2024

## I initially set out to emulate [my friends website](cbu3d.com) as closely as I reasonably could. 

I was not too worried about the fancy zooming on scoll action, but I VERY much wanted the static background that made it look like the sections were windows to each visual reality. I really enjoyed that about it

Unfortunately, because I got so deep into tweaking it and going back and forth on different approaches, I cant really show you the progression of how this went. Ultimately tho, the issue was mainly to do with this simple declaration

            position: static;

For reasons I am still going to be figuring out, this gives me the fucntionality I want, but for ONLY ONE of the looping videos. What I mean by that is no matter how I size things, how many divs I nest it in, once any or all of the videos are set to static, it will only show one of them over top others. 

            <!-- Showcase -->
		<section class="showcase">
			<div class="showcase-div" style="--video-index: 0;">
			  <div class="showcase-container">
				<video class="showcase-videosrc" playsinline preload="auto" muted loop autoplay src="/videos/CF_FlyinAround-720.mp4" type="video/mp4">
				  your browser does not support the video tag

(just imagine there are two showcase-div divs with all the appropriate end tags, Just wanted to save space here)

As you can see, I was trying my tactic of simply nesting it and trying CSS declarations on those nested divs, but sadly It also doesn't seem to matter which div class I put this declaration in, it will override any z-positioning. My theory is that position: static; puts the object in a separate sort of "space" that is reserved for any other objects set to static, which I guess does kind of make sense, but none of the other positioning method declarations seem to get me the result I want. Obviously its possible somehow, since my friends website does it, but it may be beyong simple CSS declarations...

Ultimately, I wanted to at least showcase my intention, so I left it functioning with just the one, which I will admit isn't all that terrible. 

Another day, possibly sometime soon, I will figure this out and will have the cool artsy showcase section of my dreams!

 # Footer

 # Not much to say here. Just a basic footer with all the appropriate text modifications

            <!-- Footer -->
			<footer id="footer">

				<!-- Icons -->
					<ul class="icons">
						<li><a href="https://twitter.com/cadofoxofficial/" class="icon brands fa-twitter"><span class="label">Twitter</span></a></li>
						<li><a href="https://instagram.com/cadofox/" class="icon brands fa-instagram"><span class="label">Instagram</span></a></li>
						<li><a href="https://www.linkedin.com/in/cadofox/" class="icon brands fa-linkedin-in"><span class="label">LinkedIn</span></a></li>
						<li><a href="https://www.linktr.ee/cadofox/" class="icon brands fa-external-link-alt:before"><span class="label">Linktree</span></a></li>
						<li><a href="https://www.soundcloud.com/cadofox/" class="icon brands fa-soundcloud:before"><span class="label">Soundcloud</span></a></li>

					</ul>

				<!-- Menu -->
					<ul class="menu">
						<li>&copy; CadoFox 2024</li><li>Template: <a href="https://html5up.net">HTML5 UP</a></li>
					</ul>

			</footer>

Not much to say here other than this template made these sections quite easy, but also taught me on how to put together these simple elements in more sophisticated ways! I did have to cut my losses a little bit, because it seems this template employs some sort of library of icons, instead of just a pack of transparent images. I did not find ones for things like soundcloud or linktree, so down the line I plan to just replace all of those with images. For now, I updated the href of each one that they do have that i could use with the appropriate link, so it is still functional!

# Custom CSS!

Initially I was working in the existing main.CSS that came with the template, which was all fine and good, except I really did not like clutting the already massive CSS from the template. A quick google seach revealed that all I had to do was add another one of these:

            <link rel="stylesheet" href="assets/css/custom.css" />

and boom, I could have a whole other sheet with all the custom classes, IDs, fonts, etc, neatly tucked away in its own separate style sheet! Very cool, helped a lot with organization and keeping track of my changes.

# A Word on Fonts

## Custom fonts were not as simple as I imagined, but also not that hard

One thing I did NOT want to settle for was the default fonts available for websites. I am a big typography guy, I LOVE interesting looking fonts and lettering, so I was SET on figuring out how to use custom fonts

I have a pretty big library of fonts that I use for my designs already, so initially I thought it would be as simple as adding those .oft files into the repo

no

Basically, I learned that fonts need to be converted into a "webfont" version before they can be used, which I suppose makes sense. Thankfully, theres a couple websites that do this for free, so I converted a BUNCH that I wanted to try out. 

Adding them to the website invloved adding a bunch of these to the CSS:

            @font-face {
                font-family: 'adedisplay';
                src: url('/assets/webfonts/AdeDisplay/ade-display-webfont.woff2') format('woff2'),
                    url('/assets/webfonts/AdeDisplay/ade-display-webfont.woff') format('woff'),
                }

I did run into some issues with the way it handles updating what the CSS can see in-browser, so it would just not actually use the font, despite me seeing it in the CSS in chromes element inspector. Ultimately, I got it to work tho. I have a bunch of fonts still in the repo, but ultimately decided on just one for the whole website, which I think looks just fine :)

# A Word on ChatGPT

I did try quite a few variations of asking it specific quiestions surrounding solving the showcase section issues, however literally none of it worked because it simple did not understand what I was asking it. After a few tries, I gave up, as I was getting nowhere and learning nothing, so none of that HTML or CSS was of any use other than how to NOT do what I was trying to do haha

## Future Plans

As I get better at website building, I think eventually I will want a much more interesting advanced design, however, my more immediate plans for this would be

- A working showcase section as I wanted
- A "music" section with a streaming platform connected embedded player for users to preview some of my stuff
- Customized animations; more advanced interesting ways to go from section to section
- Maybe a live feed of my instagram of some sort??

# Closing Thoughts

In all honesty, the template REALLY helped with getting a head start. I was quite surprised to find one as close to what I was after as Big Picture. All things considered, it didn't take me all that much to poke around and decipher the quite sophisticated CSS structure to find the places where I needed to modify. Working with this template has actually been super great for learning how advanced websites are built, so its been a great experience.

I will say I fully intend to continue to explore this template over time, as I think it will be good for being able to build these from scratch myself one day. A lot of the fancy animations and scripts still don't quite make sense to me, but one day they will! For now, the template allows me to have a pretty neat looking, functional, basic website for my work!

## Resources Used

- [template](https://html5up.net/uploads/demos/big-picture/)
- W3Schools
- Poking around [friend's website](cbu3d.com)
- ChatGPT (not really)
- Various google results

