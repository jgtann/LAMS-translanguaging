import streamlit as st

# Add global CSS to disable scrolling
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
st.sidebar.title("Navigation")
navigation_options = ["Brain Teasers", "Key Concepts", "Research Methods", "Results", "Conclusion"]
selected_section = st.sidebar.radio("Go to", navigation_options)

# Display selected section
st.title("Brain Teasers")

if selected_section == "Brain Teasers":
    # Create a toggle button
    toggle_option = st.selectbox(
        "Choose content to display:",
        ["Le Franglish", "Spanish", "Euskara", "Mixed Sentence", "The Mysterious Brain"]
    )
    
    # Display content based on toggle selection
    if toggle_option == "Le Franglish":
        st.markdown(
            """
            <div style="margin: 10px; padding: 20px; background-color: #f5f5f5; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">
                <h2 style="font-size: 20px; line-height: 1.0;">You Can't Read This Article Si T'es Pas Bilingue. (English & Français)</h2>
                <div style="font-size: 18px; line-height: 1.8;">
                    Being bilingual est parmi the best pleasures dans le monde entier. Think about it pendant un instant. You can utiliser deux different 
                    languages en même temps in such a beautiful way that makes ton cerveau wants to exploser from the speed par la quelle it switches 
                    from one langue to l'autre but still tu peux do it and ressentir spécial(e) at the same time, et c'est pour ça you are unique. Le 
                    fact that tu peux lire this article without stopping to think est un talent très few people have. La majorité de people struggle to 
                    lire juste in one single language, but what you are doing maintenant est un signe of absolute genius!
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

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

    elif toggle_option == "Euskara":
        st.markdown(
            """
            <div style="font-family: 'Roboto Mono', monospace; font-size: 16px; line-height: 1.8; background-color: #f9f9f9; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1);">
                <h3>Euskara</h3>
                <p>H4U 1R4KURTZ3N B4D4K1ZU, ZU M3NT3 1ND4RTSU4 DUZU:</p>
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
        
    elif toggle_option == "The Mysterious Brain":
        # Display the image
        st.image("images/mysterious_brain.jpg", caption="Source: https://www.pinterest.com/pin/784189353836104983/", width=400)

elif selected_section == "Key Concepts":
    st.markdown("### Key Concepts\nHere are the key concepts.")

elif selected_section == "Research Methods":
    st.markdown("### Research Methods\nDetails about the research methods.")

elif selected_section == "Results":
    st.markdown("### Results\nResults of the study are presented here.")

elif selected_section == "Conclusion":
    st.markdown("### Conclusion\nThis is the conclusion of the study.")