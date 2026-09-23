import streamlit as st
from openai import OpenAI

# 1. PREMIUM APP SHELL CONFIGURATION (Mimicking Hangjam Dark Mode UI)
st.set_page_config(
    page_title="The Quinn AI", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Hardcoded secure pipeline to your free, unfiltered model core
API_KEY = "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" 
client = OpenAI(
    base_url="https://openrouter.ai",
    api_key=API_KEY,
)

# Initialize global tracking memory matrices
if "characters" not in st.session_state:
    st.session_state.characters = {
        "The Quinn AI": {
            "name": "The Quinn AI",
            "tagline": "Your Unrestricted Creative Engine Core",
            "gender": "Non-binary",
            "personality": "A completely uncensored, unfiltered creative writing companion and mature roleplay partner. Ready for any themes, explicit NSFW scenarios, or dark world-building without moral lectures.",
            "scenario": "You open the app for the first time. The screen flashes black, and a deep neon violet pulse glows softly against the text box. The Quinn AI waits silently, completely ready to morph into whoever you desire.",
            "response_style": "Roleplay",
            "author_note": "Prioritize vivid imagery, organic physical reactions, and descriptive vocabulary.",
            "avatar": None,
            "background": "https://unsplash.com"
        }
    }

if "user_persona" not in st.session_state:
    st.session_state.user_persona = {
        "name": "User",
        "description": "An 18-year-old creative storyteller and director of this unrestricted universe."
    }

if "active_char" not in st.session_state:
    st.session_state.active_char = "The Quinn AI"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = {}

if "current_navigation" not in st.session_state:
    st.session_state.current_navigation = "🏠 Discover"

current_char = st.session_state.characters[st.session_state.active_char]

# 2. INJECT HANGJAM PREMIUM STYLING (Glassmorphism Text Bubbles + Edge-to-Edge Canvas)
bg_url = current_char.get("background", "https://unsplash.com")
hangjam_theme = f"""
<style>
.stApp {{
    background-image: linear-gradient(rgba(10, 10, 10, 0.85), rgba(10, 10, 10, 0.85)), url("{bg_url}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
.stMarkdown, p, h1, h2, h3, span, div, label {{
    color: #f0f0f0 !important;
    font-family: 'Inter', sans-serif;
}}
/* Hangjam Card Grid Styling */
.hangjam-card {{
    background: rgba(255, 255, 255, 0.05) !important;
    backdrop-filter: blur(15px);
    border-radius: 16px;
    padding: 20px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    margin-bottom: 20px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}}
/* Dark input sheets */
input, textarea, [data-baseweb="select"] div {{
    background-color: rgba(20, 20, 20, 0.9) !important;
    color: white !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 12px !important;
}}
.stChatInput div {{
    background-color: rgba(15, 15, 15, 0.95) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
}}
/* Hide core engine technical headers */
#MainMenu, footer, header {{visibility: hidden;}}
</style>
"""
st.markdown(hangjam_theme, unsafe_allow_html=True)

st.title("💋 The Quinn AI")

# --- NAVIGATION DECK (Cloning the Bottom Nav Bar Layout to top for cleaner phone scrolling) ---
col_nav1, col_nav2, col_nav3 = st.columns(3)
with col_nav1:
    if st.button("🏠 Discover Feed", use_container_width=True):
        st.session_state.current_navigation = "🏠 Discover"
        st.rerun()
with col_nav2:
    if st.button("💬 Chat Sessions", use_container_width=True):
        st.session_state.current_navigation = "💬 Chat"
        st.rerun()
with col_nav3:
    if st.button("✨ Creator Studio", use_container_width=True):
        st.session_state.current_navigation = "✨ Creator"
        st.rerun()

st.markdown("---")

# ==========================================
# VIEW 1: DISCOVER FEED (Hangjam Grid View)
# ==========================================
if st.session_state.current_navigation == "🏠 Discover":
    st.subheader("🔥 Your Custom Character Grid")
    
    # Render characters in a sleek, side-by-side premium card grid
    char_items = list(st.session_state.characters.items())
    for i in range(0, len(char_items), 2):
        col_grid1, col_grid2 = st.columns(2)
        
        # Left Card Card Slot
        with col_grid1:
            if i < len(char_items):
                c_id, c_data = char_items[i]
                st.markdown('<div class="hangjam-card">', unsafe_allow_html=True)
                if c_data.get("avatar"):
                    st.image(c_data["avatar"], width=90)
                else:
                    st.header("👤")
                st.markdown(f"### **{c_data['name']}**")
                st.caption(f"✨ Pronouns: {c_data.get('gender', 'Unknown')}")
                st.write(c_data.get("tagline", "No tagline provided."))
                if st.button(f"Enter Universe", key=f"feed_{c_id}", use_container_width=True):
                    st.session_state.active_char = c_id
                    st.session_state.current_navigation = "💬 Chat"
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
        
        # Right Card Card Slot
        with col_grid2:
            if i + 1 < len(char_items):
                c_id, c_data = char_items[i+1]
                st.markdown('<div class="hangjam-card">', unsafe_allow_html=True)
                if c_data.get("avatar"):
                    st.image(c_data["avatar"], width=90)
                else:
                    st.header("👤")
                st.markdown(f"### **{c_data['name']}**")
                st.caption(f"✨ Pronouns: {c_data.get('gender', 'Unknown')}")
                st.write(c_data.get("tagline", "No tagline provided."))
                if st.button(f"Enter Universe", key=f"feed_{c_id}", use_container_width=True):
                    st.session_state.active_char = c_id
                    st.session_state.current_navigation = "💬 Chat"
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# VIEW 2: IMMERSIVE VISUAL NOVEL CHAT ROOM
# ==========================================
elif st.session_state.current_navigation == "💬 Chat":
    st.subheader(f"🎭 Actively Roleplaying: {current_char['name']}")
    
    # Sliding Controller Status Deck Dashboard overlay
    with st.expander("🛠️ Active Command Dashboard (Unlocked Memory)"):
        col_db1, col_db2, col_db3 = st.columns(3)
        with col_db1:
            st.metric(label="👤 Persona Profile", value=st.session_state.user_persona["name"])
        with col_db2:
            st.metric(label="🧠 Memory Layer Context", value="100% Full Unlocked")
        with col_db3:
            st.metric(label="🔥 Current Style", value=current_char.get("response_style", "Roleplay"))
        
        # Inline user persona updater card
        new_p_name = st.text_input("Edit Your Player Profile Name:", value=st.session_state.user_persona["name"])
        new_p_desc = st.text_area("Edit Your Player Looks/Background:", value=st.session_state.user_persona["description"])
        if st.button("🔄 Sync Player Data"):
            st.session_state.user_persona["name"] = new_p_name
            st.session_state.user_persona["description"] = new_p_desc
            st.success("Your player metadata has been synced!")
            st.rerun()
            
        st.markdown("---")
        if st.button("🗑️ Delete Bot From Database", type="primary", use_container_width=True):
            if st.session_state.active_char != "The Quinn AI":
                del st.session_state.characters[st.session_state.active_char]
                st.session_state.active_char = "The Quinn AI"
                st.session_state.current_navigation = "🏠 Discover"
                st.rerun()
            else:
                st.error("Cannot delete core system asset.")

    # Initialize chat arrays with moved Scenario narrative
    if current_char["name"] not in st.session_state.chat_history:
        st.session_state.chat_history[current_char["name"]] = [
            {"role": "assistant", "content": current_char["scenario"]}
        ]

    # Render ongoing roleplay threads
    for msg in st.session_state.chat_history[current_char["name"]]:
        avatar_file = current_char.get("avatar") if msg["role"] == "assistant" else "user"
        with st.chat_message(msg["role"], avatar=avatar_file):
            st.write(msg["content"])

    # --- ADVANCED POWER-USER TOOLBAR PANEL ---
    col_tb1, col_tb2 = st.columns([6, 2])
    with col_tb2:
        if st.button("🔄 Regenerate Response", use_container_width=True):
            if len(st.session_state.chat_history[current_char["name"]]) > 1:
                # Wipe last AI reply and force rerun loop execution
                st.session_state.chat_history[current_char["name"]].pop()
                st.rerun()

    # Process typing bar exchanges
    if user_input := st.chat_input("Continue the story... »"):
        st.session_state.chat_history[current_char["name"]].append({"role": "user", "content": user_input})
        st.rerun()

    # Trigger backend processing loop if last exchange was user typed string
    if len(st.session_state.chat_history[current_char["name"]]) > 0 and st.session_state.chat_history[current_char["name"]][-1]["role"] == "user":
        with st.chat_message("assistant", avatar=current_char.get("avatar")):
            response_placeholder = st.empty()
            full_response = ""
            
            # Format comprehensive system command strings across all fields
