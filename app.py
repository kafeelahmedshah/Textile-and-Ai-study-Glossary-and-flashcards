import random
import streamlit as st

st.set_page_config(
    page_title="Textile & AI Study Glossary",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------- DATA ---------------------------------
TERMS = [
    # Textile
    {"term": "Fiber", "category": "Textile", "definition": "A fine, hair-like material that can be spun into yarn and used to make textile products.", "example": "Cotton, wool and polyester are textile fibers."},
    {"term": "Natural Fiber", "category": "Textile", "definition": "A fiber obtained from natural sources such as plants, animals or minerals.", "example": "Cotton and wool are natural fibers."},
    {"term": "Synthetic Fiber", "category": "Textile", "definition": "A man-made fiber produced mainly through chemical processes.", "example": "Polyester and nylon are synthetic fibers."},
    {"term": "Cotton", "category": "Textile", "definition": "A natural cellulosic seed-hair fiber widely used in clothing and home textiles.", "example": "Cotton is commonly used in shirts and bedsheets."},
    {"term": "Polyester", "category": "Textile", "definition": "A synthetic polymer fiber known for strength, durability and wrinkle resistance.", "example": "Polyester is often blended with cotton."},
    {"term": "Yarn", "category": "Textile", "definition": "A continuous strand of fibers or filaments used to produce fabric.", "example": "Yarn is made by spinning fibers or assembling filaments."},
    {"term": "Spinning", "category": "Textile", "definition": "The process of converting staple fibers into yarn by drafting and twisting.", "example": "Ring spinning is a common yarn manufacturing system."},
    {"term": "Blow Room", "category": "Textile", "definition": "The opening, cleaning, mixing and preparation section at the start of cotton spinning.", "example": "The blow room removes a large portion of trash from cotton."},
    {"term": "Carding", "category": "Textile", "definition": "A process that separates, cleans and aligns fibers to form a continuous web or sliver.", "example": "Carding is often called the heart of spinning."},
    {"term": "Combing", "category": "Textile", "definition": "A process that removes short fibers and remaining impurities to produce a more uniform fiber strand.", "example": "Combed yarn is generally smoother and more uniform."},
    {"term": "Drawing", "category": "Textile", "definition": "A process in which several slivers are combined and drafted to improve evenness and parallelization.", "example": "Drawing helps reduce variation in sliver thickness."},
    {"term": "Sliver", "category": "Textile", "definition": "A loose, untwisted strand of fibers produced by carding or drawing.", "example": "Card sliver is fed to the drawing frame."},
    {"term": "Roving", "category": "Textile", "definition": "A slightly twisted, attenuated strand of fibers produced before final spinning.", "example": "The roving frame prepares material for the ring frame."},
    {"term": "Weaving", "category": "Textile", "definition": "The fabric formation process in which two sets of yarns interlace at right angles.", "example": "Warp and weft yarns form woven fabric."},
    {"term": "Warp", "category": "Textile", "definition": "The lengthwise yarns running along the direction of fabric production on a loom.", "example": "Warp yarns are prepared on a beam."},
    {"term": "Weft", "category": "Textile", "definition": "The crosswise yarn inserted through the warp yarns during weaving.", "example": "A shuttle or other insertion system carries the weft."},
    {"term": "Knitting", "category": "Textile", "definition": "A fabric formation method in which yarns are formed into interconnected loops.", "example": "T-shirts are commonly made from knitted fabric."},
    {"term": "GSM", "category": "Textile", "definition": "Grams per square metre; a measure of fabric mass per unit area.", "example": "A fabric of 180 GSM has a mass of 180 grams per square metre."},
    {"term": "Yarn Count", "category": "Textile", "definition": "A numerical expression of yarn fineness or coarseness.", "example": "In the English cotton count system, a higher Ne value indicates finer yarn."},
    {"term": "Dyeing", "category": "Textile", "definition": "The process of applying color to textile materials using dyes.", "example": "Cotton fabric may be dyed with reactive dyes."},
    {"term": "Finishing", "category": "Textile", "definition": "Mechanical or chemical treatments applied to fabric to improve its appearance, handle or performance.", "example": "Softening and calendaring are finishing processes."},
    {"term": "Moisture Regain", "category": "Textile", "definition": "The mass of water in a material expressed as a percentage of its oven-dry mass.", "example": "Moisture regain is important in textile testing and processing."},
    {"term": "Tensile Strength", "category": "Textile", "definition": "The maximum pulling force a material can withstand before breaking.", "example": "Yarn tensile strength can be measured with a tensile tester."},
    {"term": "Fabric", "category": "Textile", "definition": "A flexible sheet material made by weaving, knitting, nonwoven formation or other textile processes.", "example": "Denim is a woven fabric."},
    # AI
    {"term": "Artificial Intelligence (AI)", "category": "AI", "definition": "A field of computing focused on creating systems that perform tasks associated with human intelligence.", "example": "AI can help detect fabric defects from images."},
    {"term": "Machine Learning (ML)", "category": "AI", "definition": "A branch of AI in which computer systems learn patterns from data to make predictions or decisions.", "example": "An ML model can predict yarn quality using production data."},
    {"term": "Deep Learning", "category": "AI", "definition": "A type of machine learning that uses multi-layered neural networks to learn complex patterns.", "example": "Deep learning can classify textile defect images."},
    {"term": "Dataset", "category": "AI", "definition": "A collection of data used to train, validate or test an AI model.", "example": "A textile dataset may contain GSM, yarn count and strength values."},
    {"term": "Algorithm", "category": "AI", "definition": "A defined sequence of steps or rules used to solve a problem or perform a task.", "example": "A classification algorithm assigns a defect label to an image."},
    {"term": "Model", "category": "AI", "definition": "A trained computational system that has learned patterns from data and can produce outputs.", "example": "A trained model can estimate fabric quality."},
    {"term": "Training", "category": "AI", "definition": "The process of teaching a model by exposing it to data and adjusting its internal parameters.", "example": "A model is trained using labelled fabric images."},
    {"term": "Supervised Learning", "category": "AI", "definition": "A machine-learning approach that learns from examples containing input data and known target labels.", "example": "Images labelled as hole, stain or broken yarn can train a defect classifier."},
    {"term": "Unsupervised Learning", "category": "AI", "definition": "A machine-learning approach that finds patterns or groups in data without supplied target labels.", "example": "It can group production records with similar characteristics."},
    {"term": "Reinforcement Learning", "category": "AI", "definition": "A learning approach in which an agent improves actions through rewards and penalties from an environment.", "example": "It can be explored for optimizing process-control decisions."},
    {"term": "Classification", "category": "AI", "definition": "A task in which a model assigns an input to one of several predefined categories.", "example": "Classifying fabric images as defect-free or defective."},
    {"term": "Regression", "category": "AI", "definition": "A task in which a model predicts a continuous numerical value.", "example": "Predicting fabric tensile strength in newtons."},
    {"term": "Neural Network", "category": "AI", "definition": "A computing model made of connected processing units arranged in layers, inspired loosely by biological neural systems.", "example": "Neural networks can learn complex relationships in textile process data."},
    {"term": "Computer Vision", "category": "AI", "definition": "An AI area that enables computers to interpret information from images and videos.", "example": "Computer vision can inspect fabric surfaces for defects."},
    {"term": "Natural Language Processing (NLP)", "category": "AI", "definition": "An AI field that helps computers process, understand and generate human language.", "example": "An NLP chatbot can answer textile terminology questions."},
    {"term": "Generative AI", "category": "AI", "definition": "AI that creates new content such as text, images, audio or code based on learned patterns.", "example": "A generative AI tool can draft a textile lab-report outline."},
    {"term": "Prompt", "category": "AI", "definition": "An instruction or input given to an AI system to guide the response or output.", "example": "A clear prompt can ask for a simple explanation of carding."},
    {"term": "Overfitting", "category": "AI", "definition": "A modelling problem in which a model learns training examples too closely and performs poorly on new data.", "example": "A defect detector may memorize training images instead of learning general patterns."},
    {"term": "Accuracy", "category": "AI", "definition": "The proportion of all predictions that a classification model gets correct.", "example": "If 90 out of 100 predictions are correct, accuracy is 90%."},
    {"term": "Prediction", "category": "AI", "definition": "An output produced by a model for new or unseen input data.", "example": "A model may predict the quality grade of a fabric sample."},
]

QUIZ = [
    {"q": "Which process separates, cleans and aligns fibers to form sliver?", "options": ["Weaving", "Carding", "Dyeing", "Finishing"], "a": "Carding", "why": "Carding opens, separates, cleans and aligns fibers."},
    {"q": "What does GSM stand for?", "options": ["General Spinning Method", "Grams per Square Metre", "Grain Size Measure", "Grams per Spun Material"], "a": "Grams per Square Metre", "why": "GSM expresses fabric mass per unit area."},
    {"q": "Which yarns run lengthwise in woven fabric?", "options": ["Weft", "Filling only", "Warp", "Sliver"], "a": "Warp", "why": "Warp yarns run in the lengthwise direction."},
    {"q": "Which AI approach learns from labelled examples?", "options": ["Unsupervised learning", "Supervised learning", "Random guessing", "Data cleaning"], "a": "Supervised learning", "why": "Supervised learning uses input examples with known labels."},
    {"q": "Which AI field works with images and videos?", "options": ["Computer Vision", "NLP", "Spinning", "Regression"], "a": "Computer Vision", "why": "Computer vision interprets visual information."},
    {"q": "Predicting a numerical value such as tensile strength is usually:", "options": ["Classification", "Regression", "Weaving", "Tokenization"], "a": "Regression", "why": "Regression predicts continuous numerical values."},
    {"q": "What is a dataset?", "options": ["A loom part", "A collection of data", "A dyeing chemical", "A type of yarn"], "a": "A collection of data", "why": "Datasets contain examples used in model development."},
    {"q": "Which fiber is a natural cellulosic seed-hair fiber?", "options": ["Nylon", "Polyester", "Cotton", "Acrylic"], "a": "Cotton", "why": "Cotton is a natural cellulosic seed-hair fiber."},
    {"q": "What is overfitting?", "options": ["Model performs well only on training data", "Fabric becomes heavier", "Yarn becomes twisted", "Data is deleted"], "a": "Model performs well only on training data", "why": "Overfitting harms performance on new, unseen data."},
    {"q": "What is a prompt?", "options": ["A fabric defect", "An instruction given to an AI system", "A yarn count", "A loom setting"], "a": "An instruction given to an AI system", "why": "A prompt guides the AI system's response."},
    {"q": "Which process forms fabric by interlacing warp and weft?", "options": ["Knitting", "Weaving", "Combing", "Drawing"], "a": "Weaving", "why": "Weaving interlaces two yarn systems at right angles."},
    {"q": "Which metric is the proportion of correct classification predictions?", "options": ["GSM", "Accuracy", "Moisture regain", "Yarn count"], "a": "Accuracy", "why": "Accuracy is correct predictions divided by total predictions."},
]

# ----------------------------- STYLE ---------------------------------
st.markdown("""
<style>
    .main {background: #f6f8fc;}
    .block-container {padding-top: 1.6rem; padding-bottom: 2rem; max-width: 1200px;}
    .hero {padding: 1.45rem 1.7rem; border-radius: 18px; color: white;
           background: linear-gradient(115deg,#102a43,#176b87 58%,#36a6a0);
           margin-bottom: 1rem;}
    .hero h1 {font-size: 2rem; margin: 0 0 .35rem 0; color: white;}
    .hero p {margin: 0; color: #e8f4f7; font-size: 1rem;}
    .term-card {background: white; border: 1px solid #e4eaf1; border-radius: 14px;
                padding: 1rem 1.1rem; margin: .45rem 0; min-height: 150px;}
    .term-card h3 {margin: .2rem 0 .5rem 0; color: #15344b; font-size: 1.12rem;}
    .muted {color: #607487; font-size: .88rem;}
    .pill {display:inline-block; background:#e7f2f5; color:#176b87; padding:.2rem .6rem;
           border-radius:20px; font-size:.75rem; font-weight:600;}
    div.stButton > button {border-radius: 10px; font-weight: 600;}
    [data-testid="stMetric"] {background:white; padding: .8rem; border:1px solid #e5ebf2; border-radius:12px;}
</style>
""", unsafe_allow_html=True)

if "flash_index" not in st.session_state:
    st.session_state.flash_index = 0
if "flash_show" not in st.session_state:
    st.session_state.flash_show = False
if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = []
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_answered" not in st.session_state:
    st.session_state.quiz_answered = False
if "quiz_selected" not in st.session_state:
    st.session_state.quiz_selected = None
if "quiz_done" not in st.session_state:
    st.session_state.quiz_done = False

st.markdown("""
<div class="hero">
  <h1>📚 Textile & AI Study Glossary</h1>
  <p>Learn key concepts, explore definitions and test your knowledge with interactive flashcards and quizzes.</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("📘 Study Menu")
    page = st.radio("Choose a section", ["Glossary", "Flashcards", "Quiz Mode"], label_visibility="collapsed")
    st.divider()
    st.caption("Project ID: 25TE091")
    st.caption("Textile Engineering + Artificial Intelligence")
    st.info("Study tip: Learn a few terms daily and use Quiz Mode to check your understanding.")

if page == "Glossary":
    st.subheader("Explore the Glossary")
    c1, c2, c3 = st.columns([2, 1, 1])
    with c1:
        search = st.text_input("🔎 Search a term or definition", placeholder="Example: carding, dataset, GSM...")
    with c2:
        category = st.selectbox("Category", ["All", "Textile", "AI"])
    with c3:
        sort_by = st.selectbox("Sort", ["A–Z", "Z–A"])

    filtered = []
    for item in TERMS:
        matches_category = category == "All" or item["category"] == category
        query = search.strip().lower()
        matches_query = not query or query in item["term"].lower() or query in item["definition"].lower() or query in item["example"].lower()
        if matches_category and matches_query:
            filtered.append(item)
    filtered.sort(key=lambda x: x["term"].lower(), reverse=(sort_by == "Z–A"))

    m1, m2, m3 = st.columns(3)
    m1.metric("Total terms", len(TERMS))
    m2.metric("Textile terms", sum(x["category"] == "Textile" for x in TERMS))
    m3.metric("AI terms", sum(x["category"] == "AI" for x in TERMS))
    st.write(f"Showing **{len(filtered)}** matching terms.")
    if filtered:
        for start in range(0, len(filtered), 2):
            cols = st.columns(2)
            for col, item in zip(cols, filtered[start:start+2]):
                with col:
                    st.markdown(f"""
                    <div class="term-card">
                      <span class="pill">{item['category']}</span>
                      <h3>{item['term']}</h3>
                      <div>{item['definition']}</div>
                      <p class="muted"><b>Example:</b> {item['example']}</p>
                    </div>
                    """, unsafe_allow_html=True)
    else:
        st.warning("No matching term found. Try another keyword or category.")

elif page == "Flashcards":
    st.subheader("🗂️ Quick Flashcards")
    st.write("Read the term, think of its meaning, then reveal the definition.")
    flash_category = st.selectbox("Choose flashcard set", ["All", "Textile", "AI"])
    cards = [x for x in TERMS if flash_category == "All" or x["category"] == flash_category]
    if st.session_state.flash_index >= len(cards):
        st.session_state.flash_index = 0
    card = cards[st.session_state.flash_index]
    st.progress((st.session_state.flash_index + 1) / len(cards))
    st.caption(f"Card {st.session_state.flash_index + 1} of {len(cards)} • {card['category']}")
    st.markdown(f"""
    <div class="term-card" style="min-height:220px; text-align:center; display:flex; flex-direction:column; justify-content:center;">
      <span class="pill">{card['category']}</span>
      <h2 style="color:#15344b; margin-top:1rem;">{card['term']}</h2>
      <p class="muted">What does this term mean?</p>
    </div>
    """, unsafe_allow_html=True)
    if st.session_state.flash_show:
        st.success(card["definition"])
        st.info("Example: " + card["example"])
    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("🔄 Reveal / Hide", use_container_width=True):
            st.session_state.flash_show = not st.session_state.flash_show
            st.rerun()
    with b2:
        if st.button("⬅ Previous", use_container_width=True):
            st.session_state.flash_index = (st.session_state.flash_index - 1) % len(cards)
            st.session_state.flash_show = False
            st.rerun()
    with b3:
        if st.button("Next ➡", type="primary", use_container_width=True):
            st.session_state.flash_index = (st.session_state.flash_index + 1) % len(cards)
            st.session_state.flash_show = False
            st.rerun()
    if st.button("🔀 Shuffle cards"):
        random.shuffle(cards)
        st.session_state.flash_index = 0
        st.session_state.flash_show = False
        st.rerun()

else:
    st.subheader("🧠 Quick Quiz Mode")
    st.write("Answer the multiple-choice questions and review your result at the end.")
    if not st.session_state.quiz_questions:
        if st.button("▶ Start Quiz", type="primary"):
            st.session_state.quiz_questions = random.sample(QUIZ, k=min(10, len(QUIZ)))
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_answered = False
            st.session_state.quiz_selected = None
            st.session_state.quiz_done = False
            st.rerun()
        st.caption(f"The quiz contains up to 10 randomly selected questions from a bank of {len(QUIZ)}.")
    elif st.session_state.quiz_done:
        total = len(st.session_state.quiz_questions)
        score = st.session_state.quiz_score
        st.success("Quiz completed!")
        st.metric("Your score", f"{score} / {total}", f"{round(score/total*100)}%")
        if score == total:
            st.balloons()
            st.write("Excellent work! You answered every question correctly.")
        elif score >= total * 0.6:
            st.write("Good effort! Review the explanations and try again.")
        else:
            st.write("Keep practising. Review the glossary and attempt another quiz.")
        if st.button("🔁 Try Another Quiz", type="primary"):
            st.session_state.quiz_questions = []
            st.session_state.quiz_done = False
            st.rerun()
    else:
        idx = st.session_state.quiz_index
        total = len(st.session_state.quiz_questions)
        question = st.session_state.quiz_questions[idx]
        st.progress((idx + 1) / total)
        st.caption(f"Question {idx + 1} of {total}")
        st.markdown(f"### {question['q']}")
        if not st.session_state.quiz_answered:
            selected = st.radio("Select one answer:", question["options"], key=f"answer_{idx}")
            if st.button("Submit Answer", type="primary"):
                st.session_state.quiz_selected = selected
                st.session_state.quiz_answered = True
                if selected == question["a"]:
                    st.session_state.quiz_score += 1
                st.rerun()
        else:
            if st.session_state.quiz_selected == question["a"]:
                st.success("Correct!")
            else:
                st.error(f"Not quite. Correct answer: {question['a']}")
            st.info(question["why"])
            if st.button("Next Question ➡", type="primary"):
                st.session_state.quiz_index += 1
                st.session_state.quiz_answered = False
                st.session_state.quiz_selected = None
                if st.session_state.quiz_index >= total:
                    st.session_state.quiz_done = True
                st.rerun()

st.divider()
st.caption("Educational study tool • Definitions are simplified for student learning • Project 25TE091")
