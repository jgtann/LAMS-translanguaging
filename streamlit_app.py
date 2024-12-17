import streamlit as st

# Disable scrolling
st.markdown(
    """
    <style>
        body {
            overflow: hidden; /* Prevent scrolling */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar navigation
selected_section = st.sidebar.radio("INTRODUCTION", ["Translanguaging", "Key Concepts", "Visualizing Translanguaging"])

if selected_section == "Translanguaging":
    # Display selected section
    st.markdown("### What is Translanguaging")
    
    # Create a toggle button
    toggle_option = st.selectbox(
        "Choose content to display:",
        ["Le Franglish", "Spanish", "Hmm...?", "Mixed Sentence", "The Mysterious Brain"]
    )
    
    # Timer HTML (for "Le Franglish")
    if toggle_option == "Le Franglish":
        st.components.v1.html(
            """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Le Franglish Timer</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        text-align: center;
                        background-color: #f9f9f9;
                        margin: 0;
                        padding: 20px;
                    }
                    .container {
                        margin: 20px auto;
                        padding: 20px;
                        max-width: 800px;
                        background-color: #ffffff;
                        border-radius: 10px;
                        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                    }
                    .timer {
                        font-size: 2em;
                        font-weight: bold;
                        color: #ff0000;
                        margin-bottom: 20px;
                    }
                    .start-button {
                        padding: 10px 20px;
                        font-size: 1em;
                        color: white;
                        background-color: #007bff;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        margin-top: 10px;
                    }
                    .start-button:hover {
                        background-color: #0056b3;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <div id="timer" class="timer">00:00</div>
                    <button class="start-button" onclick="startStopTimer()">Start Timer</button>
                    <div class="content">
                        <h2>You Can't Read This Article Si T'es Pas Bilingue. (English & Français)</h2>
                        <p>
                            Being bilingual est parmi the best pleasures dans le monde entier. Think about it pendant un instant.
                            You can utiliser deux different languages en même temps in such a beautiful way that makes ton cerveau
                            want to exploser from the speed par laquelle it switches from one langue to l'autre but still tu peux do
                            it and ressentir spécial(e) at the same time. Et c'est pour ça you are unique.
                        </p>
                    </div>
                </div>
                <script>
                    let timerInterval;
                    let isRunning = false;
                    let elapsedSeconds = 0;

                    function startStopTimer() {
                        const timerElement = document.getElementById("timer");
                        if (isRunning) {
                            clearInterval(timerInterval);
                            isRunning = false;
                        } else {
                            isRunning = true;
                            timerInterval = setInterval(() => {
                                elapsedSeconds++;
                                const minutes = Math.floor(elapsedSeconds / 60);
                                const seconds = elapsedSeconds % 60;
                                timerElement.textContent = `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
                            }, 1000);
                        }
                    }
                </script>
            </body>
            </html>
            """,
            height=600,
        )

    # Other options
    elif toggle_option == "Spanish":
        
        st.markdown(
            """
            <div style="font-family: 'Roboto Mono', monospace; font-size: 16px; line-height: 1.8; background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">
                <h3>Spanish</h3>
                <p>S1 PU3D35 L33R 3STO, T13N35 UN4 M3NT3 FU3RT3:</p>
                <p>3ST3 M3554J3 S1RV3 P4R4 D3M0STR4R L4 C4P4C1D4D D3 L4 M3NT3.<br>
                4L PR1NC1P10 P4R3C3 C0MPL1C4D0, P3R0 4H0R4 TU M3NT3 L0 L33<br>
                4UT0M4T1C4M3NT3 S1N S1QU13R4 P3N54RL0.<br>
                ¡S3 F3L1Z!<br>
                SÓL0 4LGUN4S P3RS0N4S PU3D3N H4C3RL0.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    elif toggle_option == "Hmm...?":

        st.markdown(
            """
            <div style="font-family: 'Roboto Mono', monospace; font-size: 16px; line-height: 1.8; background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">
                <h3>???</h3>
                <p>H4U 1R4KURTZ3N B4D4K1ZU, M3NT3 1ND4RTSU4 DUZU:</p>
                <p>M3ZU H4U ZUR3 6URMU4K Z3N8T N4H1 M4IT3R D34.<br>
                H45I4N Z4IL4 Z3N, B41N4 0R41N ZUR3 6URMU4<br>
                AUT0M4T1KOK1 1R4KURTZ3N 4R1 D4.<br>
                H4RROT4 1Z4N!<br>
                GUTXI K0NTZ3NTR4TUT4K 1R4KURT34 L3KU4N.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif toggle_option == "Mixed Sentence":
                # Embed custom HTML and CSS for the updated visual
        st.components.v1.html(
            """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Mixed Language Visual</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        text-align: center;
                        background-color: #f9f9f9;
                    }
                    .highlight {
                        font-size: 2em;
                        font-weight: bold;
                        margin: 20px;
                        line-height: 1.5;
                    }
                    .highlight span {
                        display: inline-block;
                        position: relative;
                    }
                    .tamil { color: green; }
                    .mandarin { color: #e4007c; }
                    .cantonese { color: red; }
                    .english { color: deepskyblue; }
                    .malay { color: blue; }
                    .hokkien { color: purple; }
                    .unknown { color: goldenrod; }

                    .kopitiam span {
                        display: inline;
                        white-space: nowrap; /* Ensure word stays together */
                    }

                    .translation {
                        font-size: 1.2em;
                        margin-top: 20px;
                        color: gray;
                    }
                </style>
            </head>
            <body>
                <div class="highlight">
                    <span class="tamil">Dey</span>, 
                    <span class="mandarin">wǒ men</span> 
                    <span class="cantonese">paktor</span> 
                    <span class="english">always</span> 
                    <span class="malay">makan</span> 
                    <span class="english">at</span> 
                    <span class="kopitiam">
                        <span class="malay">kopi</span><span class="hokkien">tiam</span>
                    </span>
                    <span class="unknown">one</span>.
                </div>
                <div class="translation">
                    Translation: Hey, when we date we always eat at the coffeeshop (one).
                </div>
            </body>
            </html>
            """,
            height=300,
        )

        st.caption("(Source: Article titled 'I grew up in Singapore and have lived here all my life - \
                   here's my complete guide to visiting the island-state,' by Sam David published in Business Insider on 11 Oct 2022.)")

    elif toggle_option == "The Mysterious Brain":
        st.image("images/mysterious_brain.jpg", caption="The Mysterious Brain", width=400)

elif selected_section == "Visualizing Translanguaging":

    # Title
    st.title("Visualizing Translanguaging")

    # Embed HTML, CSS, and JavaScript
    st.components.v1.html(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Slide Transition</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f9f9f9;
                    overflow: hidden;
                    text-align: center;
                }

                .slide-container {
                    position: relative;
                    width: 100%;
                    height: 300px;
                    margin: auto;
                    overflow: hidden;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    background-color: white;
                }

                .slide {
                    position: absolute;
                    width: 100%;
                    height: 100%;
                    opacity: 0;
                    transition: opacity 1s ease-in-out;
                }

                .slide.active {
                    opacity: 1;
                }

                .buttons {
                    margin: 20px;
                }

                table {
                    width: 80%;
                    margin: 20px auto;
                    border-collapse: collapse;
                }

                th, td {
                    border: 1px solid #ddd;
                    padding: 10px;
                    text-align: center;
                }

                th {
                    background-color: #4CAF50;
                    color: white;
                }

                td {
                    background-color: #f9f9f9;
                }

                caption {
                    font-size: 1.2em;
                    margin: 10px;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class="slide-container">
                <!-- Slide 1 -->
                <div class="slide active" id="slide1">
                    <table>
                        <caption>in comparison with Code Switching and Hetereglossia</caption>
                        <tr>
                            <th>Concept</th>
                            <th>Language Boundaries*</th>
                        </tr>
                        <tr>
                            <td>Translanguaging</td>
                            <td>No</td>
                        </tr>
                        <tr>
                            <td>Code Switching</td>
                            <td>Yes</td>
                        </tr>
                        <tr>
                            <td>Heteroglossia</td>
                            <td>No</td>
                        </tr>
                    </table>
                </div>

                <!-- Slide 2 -->
                <div class="slide" id="slide2">
                    <table>
                        <caption>Translanguaging, Code Switching and Hetereglossia</caption>
                        <tr>
                            <th>Concept</th>
                            <th>Language Boundaries*</th>
                            <th>As a Pedagogical Strategy</th>
                        </tr>
                        <tr>
                            <td>Translanguaging</td>
                            <td>No</td>
                            <td>Yes</td>
                        </tr>
                        <tr>
                            <td>Code Switching</td>
                            <td>Yes</td>
                            <td>Yes</td>
                        </tr>
                        <tr>
                            <td>Heteroglossia</td>
                            <td>No</td>
                            <td>No</td>
                        </tr>
                    </table>
                </div>
            </div>

            <!-- Navigation Buttons -->
            <div class="buttons">
                <button onclick="showSlide(1)">Slide 1</button>
                <button onclick="showSlide(2)">Slide 2</button>
            </div>

            <script>
                function showSlide(slideNumber) {
                    const slides = document.querySelectorAll('.slide');
                    slides.forEach((slide, index) => {
                        if (index === slideNumber - 1) {
                            slide.classList.add('active');
                        } else {
                            slide.classList.remove('active');
                        }
                    });
                }
            </script>
        </body>
        </html>
        """,
        height=400,
    )

elif selected_section == "Translanguaging":

    # Add buttons for control
    start_button = st.button("Start Animation")
    stop_button = st.button("Stop Animation")

    # Embed HTML, CSS, and JavaScript
    st.components.v1.html(
        f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Particle Animation</title>
            <style>
                body {{
                    margin: 0;
                    padding: 0;
                    overflow: hidden;
                    background-color: #000;
                }}
                canvas {{
                    display: block;
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                }}
            </style>
        </head>
        <body>
            <canvas id="canvas1"></canvas>
            <script>
                const canvas = document.getElementById("canvas1");
                const ctx = canvas.getContext("2d");
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;

                let particlesArray = [];
                let animationActive = {"true" if start_button else "false"};
                let stopAnimation = {"true" if stop_button else "false"};

                // Get mouse position
                let mouse = {{
                    x: null,
                    y: null,
                    radius: (canvas.height / 80) * (canvas.width / 80),
                }};

                window.addEventListener("mousemove", function (event) {{
                    mouse.x = event.x;
                    mouse.y = event.y;
                }});

                // Create Particle class
                class Particle {{
                    constructor(x, y, directionX, directionY, size, color) {{
                        this.x = x;
                        this.y = y;
                        this.directionX = directionX;
                        this.directionY = directionY;
                        this.size = size;
                        this.color = color;
                    }}

                    draw() {{
                        ctx.beginPath();
                        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);
                        ctx.fillStyle = this.color;
                        ctx.fill();
                    }}

                    update() {{
                        if (this.x > canvas.width || this.x < 0) {{
                            this.directionX = -this.directionX;
                        }}
                        if (this.y > canvas.height || this.y < 0) {{
                            this.directionY = -this.directionY;
                        }}

                        let dx = mouse.x - this.x;
                        let dy = mouse.y - this.y;
                        let distance = Math.sqrt(dx * dx + dy * dy);
                        if (distance < mouse.radius + this.size) {{
                            if (mouse.x < this.x && this.x < canvas.width - this.size * 10) {{
                                this.x += 10;
                            }}
                            if (mouse.x > this.x && this.x > this.size * 10) {{
                                this.x -= 10;
                            }}
                            if (mouse.y < this.y && this.y < canvas.height - this.size * 10) {{
                                this.y += 10;
                            }}
                            if (mouse.y > this.y && this.y > this.size * 10) {{
                                this.y -= 10;
                            }}
                        }}

                        this.x += this.directionX;
                        this.y += this.directionY;

                        this.draw();
                    }}
                }}

                function init() {{
                    particlesArray = [];
                    let numberOfParticles = (canvas.height * canvas.width) / 9000;
                    for (let i = 0; i < numberOfParticles; i++) {{
                        let size = Math.random() * 5 + 1;
                        let x = Math.random() * (innerWidth - size * 2) + size * 2;
                        let y = Math.random() * (innerHeight - size * 2) + size * 2;
                        let directionX = Math.random() * 5 - 2.5;
                        let directionY = Math.random() * 5 - 2.5;
                        let color = "#8C5523";

                        particlesArray.push(new Particle(x, y, directionX, directionY, size, color));
                    }}
                }}

                function connect() {{
                    for (let a = 0; a < particlesArray.length; a++) {{
                        for (let b = a; b < particlesArray.length; b++) {{
                            let distance =
                                Math.pow(particlesArray[a].x - particlesArray[b].x, 2) +
                                Math.pow(particlesArray[a].y - particlesArray[b].y, 2);
                            if (distance < (canvas.width / 7) * (canvas.height / 7)) {{
                                let opacityValue = 1 - distance / 20000;
                                ctx.strokeStyle = `rgba(140,85,31,${{opacityValue}})`;
                                ctx.lineWidth = 1;
                                ctx.beginPath();
                                ctx.moveTo(particlesArray[a].x, particlesArray[a].y);
                                ctx.lineTo(particlesArray[b].x, particlesArray[b].y);
                                ctx.stroke();
                            }}
                        }}
                    }}
                }}

                function animate() {{
                    if (!animationActive || stopAnimation) return;
                    ctx.clearRect(0, 0, canvas.width, canvas.height);
                    for (let i = 0; i < particlesArray.length; i++) {{
                        particlesArray[i].update();
                    }}
                    connect();
                    requestAnimationFrame(animate);
                }}

                window.addEventListener("resize", function () {{
                    canvas.width = innerWidth;
                    canvas.height = innerHeight;
                    mouse.radius = (canvas.height / 80) * (canvas.width / 80);
                    init();
                    if (stopAnimation) {{
                        drawFrozenState();
                    }}
                }});

                window.addEventListener("mouseout", function () {{
                    mouse.x = undefined;
                    mouse.y = undefined;
                }});

                function drawFrozenState() {{
                    particlesArray.forEach((particle) => particle.draw());
                    connect();
                }}

                // Initialize particles
                init();

                if (animationActive) {{
                    animate();
                }}

                if (stopAnimation) {{
                    drawFrozenState();
                }}
            </script>
        </body>
        </html>
        """,
        height=600,
    )

elif selected_section == "Research Methods":
    st.markdown("### Research Methods\nDetails about the research methods.")

    # HTML + CSS + JavaScript for Slide Transition
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Translanguaging Presentation</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #f8ffe6;
                color: #333;
                text-align: center;
                overflow: hidden;
            }
            .slide-container {
                width: 100%;
                height: 100vh;
                position: relative;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .slide {
                position: absolute;
                opacity: 0;
                transition: opacity 1s ease-in-out;
            }
            .slide.active {
                opacity: 1;
            }
            h1, h2, h3 {
                margin: 10px;
            }
            .title-bar {
                position: absolute;
                top: 20px;
                left: 20px;
                font-size: 1.2em;
                font-weight: bold;
                text-align: left;
            }
            .start-button, .nav-button {
                padding: 10px 20px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 1em;
                margin: 10px;
            }
            .start-button:hover, .nav-button:hover {
                background-color: #0056b3;
            }
            .footer {
                position: absolute;
                bottom: 20px;
                left: 50%;
                transform: translateX(-50%);
                font-size: 0.9em;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div id="slides">
            <!-- Slide 1: Title Slide -->
            <div class="slide active" id="slide1">
                <h1><strong>TRANSLANGUAGING IN THE BILINGUAL CLASSROOM</strong></h1>
                <h2>A PEDAGOGY FOR LEARNING AND TEACHING?</h2>
                <h3>Creese & Blackledge (2010)</h3>
                <div class="footer">Presented by: TAN, WANJING | WARDAH BINTI ZULKURNAIN</div>
                <button class="start-button" onclick="nextSlide()">Start</button>
            </div>

            <!-- Slide 2: Overview -->
            <div class="slide" id="slide2">
                <h2>Overview</h2>
                <ul style="list-style: none; font-size: 1.2em;">
                    <li>01: INTRODUCTION</li>
                    <li>02: PROBLEM</li>
                    <li>03: LITERARY PREVIEW</li>
                    <li>04: THEORETICAL</li>
                    <li>05: OBJECTIVES</li>
                    <li>06: METHODOLOGY</li>
                    <li>07: IMPLEMENTATION</li>
                    <li>08: RESULTS</li>
                    <li>09: CONCLUSION</li>
                    <li>10: RECOMMENDATIONS</li>
                </ul>
                <button class="nav-button" onclick="prevSlide()">Previous</button>
                <button class="nav-button" onclick="nextSlide()">Next</button>
            </div>

            <!-- Slide 3: Complementary Schools -->
            <div class="slide" id="slide3">
                <h2>Complementary Schools</h2>
                <p>Established by <strong>community members</strong></p>
                <p>Focus: Teaching <strong>language, culture, and heritage</strong> to complement statutory education.</p>
                <button class="nav-button" onclick="prevSlide()">Previous</button>
                <button class="nav-button" onclick="nextSlide()">Next</button>
            </div>

            <!-- Add More Slides Here -->
        </div>

        <script>
            const slides = document.querySelectorAll('.slide');
            let currentSlide = 0;

            function showSlide(index) {
                slides.forEach((slide, i) => {
                    slide.classList.remove('active');
                    if (i === index) {
                        slide.classList.add('active');
                    }
                });
            }

            function nextSlide() {
                currentSlide = (currentSlide + 1) % slides.length;
                showSlide(currentSlide);
            }

            function prevSlide() {
                currentSlide = (currentSlide - 1 + slides.length) % slides.length;
                showSlide(currentSlide);
            }

            showSlide(currentSlide);
        </script>
    </body>
    </html>
    """

    # Streamlit Component to Embed HTML Code
    st.components.v1.html(html_code, height=600)

elif selected_section == "Results":
    st.markdown("### Results\nResults of the study are presented here.")

elif selected_section == "Conclusion":
    st.markdown("### Conclusion\nThis is the conclusion of the study.")