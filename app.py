import streamlit as st
from helper_function import get_diagnosis, get_treatment_plan

st.title("AI-Powered Medical Diagnosis Assistant")

symptoms = st.text_area("Enter patient symptoms", "e.g., fever, cough, sore throat")

if st.button("Diagnose"):
    if symptoms:
        diagnosis = get_diagnosis(symptoms)
        if "error" in diagnosis:
            st.error(f"Error: {diagnosis['error']}")
        else:
            st.subheader(f"Diagnosis: {diagnosis['diagnosis']}")
            treatment_plan = get_treatment_plan(diagnosis['diagnosis'])
            if "error" in treatment_plan:
                st.error(f"Error: {treatment_plan['error']}")
            else:
                st.subheader("Suggested Treatment Plan")
                st.write(treatment_plan)
    else:
        st.error("Please enter symptoms to diagnose.")
