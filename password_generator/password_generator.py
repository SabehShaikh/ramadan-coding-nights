import streamlit as st
import random
import string
import re

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits: characters += string.digits
    if use_special: characters += string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8: 
        score += 1
    else: 
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password): 
        score += 1
    else: 
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password): 
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    if re.search(f"[{re.escape(string.punctuation)}]", password): 
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    if score == 4:
        return "✅ Strong Password!", feedback
    elif score == 3:
        return "⚠️ Moderate Password", feedback
    else: 
        return "❌ Weak Password", feedback


st.set_page_config(page_title="Password Tool", page_icon="🔐")

# App header
st.title("🔐 Password Generator & Strength Meter")
st.write("Create secure passwords and analyze their strength with this tool.")


tab1, tab2 = st.tabs(["Generate Password", "Check Password"])

# Tab 1: Password Generator
with tab1:
    st.subheader("🔑 Generate a Password")
    length = st.slider("Length", 6, 32, 12)
    col1, col2 = st.columns(2)
    use_digits = col1.checkbox("Include digits", True)
    use_special = col2.checkbox("Include symbols", True)
    
    if st.button("Generate"):
        password = generate_password(length, use_digits, use_special)
        st.code(password)
        
      
        st.info("Password generated! To check its strength, go to the 'Check Password' tab.")
        
        # Store in session state for the other tab
        st.session_state.last_password = password


# Tab 2: Password Strength Checker
with tab2:
    st.subheader("🔍 Check Your Password Strength")

    # Pre-fill password if generated in Tab 1
    user_password = st.text_input(
        "Enter your password", 
        value=st.session_state.get("last_password", ""), 
        type="password"
    )

    show_password = st.checkbox("Show password", value=False)
    
    # Reveal password when checkbox is checked
    if show_password and user_password:
        st.code(user_password, language=None)

    if st.button("Check Strength", key="check_btn"):
        if user_password:
            strength, feedback = check_password_strength(user_password)
            
            if "Strong" in strength:
                st.success(f"💪 {strength}")
            elif "Moderate" in strength:
                st.warning(f"⚠️ {strength}")
            else:
                st.error(f"❌ {strength}")

            with st.expander("🔬 Detailed Analysis", expanded=True):
                st.write(f"**Password Length:** {len(user_password)} characters")

               
                has_upper = bool(re.search(r"[A-Z]", user_password))
                has_lower = bool(re.search(r"[a-z]", user_password))
                has_digit = bool(re.search(r"\d", user_password))
                has_special = bool(re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", user_password))
                
                cols = st.columns(4)
                cols[0].metric("🔠 Uppercase", "✅" if has_upper else "❌")
                cols[1].metric("🔡 Lowercase", "✅" if has_lower else "❌")
                cols[2].metric("🔢 Digits", "✅" if has_digit else "❌")
                cols[3].metric("🔣 Special Chars", "✅" if has_special else "❌")
                
                if feedback:
                    st.write("📌 **Improvement Suggestions:**")
                    for msg in feedback:
                        st.write(f"- {msg}")

        else:
            st.warning("Please enter a password to check its strength.")


# Password safety tips
with st.expander("Password Security Tips 🔒"):
    st.markdown("""
    - Use at least 12 characters, mix of letters, numbers, and symbols
    - Avoid common words or patterns
    - Use different passwords for different accounts
    - Consider using a password manager
    - Enable two-factor authentication when available
    """)            

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center;'>
        🔑 Password Tool by <a href='https://github.com/sabehshaikh'>Sabeh Shaikh</a>
    </p>
""", unsafe_allow_html=True)