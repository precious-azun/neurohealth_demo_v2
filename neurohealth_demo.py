{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "7fd88bfc-4c07-4feb-af6f-ac9639915e15",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import random\n",
    "\n",
    "st.set_page_config(page_title=\"NeuroHealthFocus Triage Demo\", layout=\"centered\")\n",
    "st.title(\"🧠 NeuroHealthFocus: Stroke Triage & Recovery\")\n",
    "\n",
    "st.markdown(\"\"\"\n",
    "This demo simulates how our AI platform could prioritize stroke patients and provide recovery suggestions—**without requiring real patient data**.\n",
    "\"\"\")\n",
    "\n",
    "# Input fields\n",
    "st.header(\"1. Enter Patient Information\")\n",
    "age = st.slider(\"Age\", 18, 100, 65)\n",
    "severity = st.selectbox(\"Stroke Severity\", [\"Mild\", \"Moderate\", \"Severe\"])\n",
    "time_since_onset = st.slider(\"Time Since Onset (in hours)\", 0, 48, 2)\n",
    "symptoms = st.multiselect(\"Symptoms\", [\"Speech difficulty\", \"Paralysis\", \"Confusion\", \"Vision loss\", \"Headache\"])\n",
    "\n",
    "# Simulate triage logic\n",
    "def simulate_triage(age, severity, time_since_onset, symptoms):\n",
    "    urgency_map = {\n",
    "        \"Severe\": \"🚨 Urgent\",\n",
    "        \"Moderate\": \"⚠️ Semi-Urgent\",\n",
    "        \"Mild\": \"⏳ Routine\"\n",
    "    }\n",
    "    if severity == \"Severe\" or time_since_onset < 3:\n",
    "        triage = urgency_map[\"Severe\"]\n",
    "    elif severity == \"Moderate\" and time_since_onset < 12:\n",
    "        triage = urgency_map[\"Moderate\"]\n",
    "    else:\n",
    "        triage = urgency_map[\"Mild\"]\n",
    "    \n",
    "    recovery_plan = {\n",
    "        \"Week 1\": \"Physical therapy & monitoring\",\n",
    "        \"Week 2\": \"Speech therapy\" if \"Speech difficulty\" in symptoms else \"Mobility training\",\n",
    "        \"Week 3\": \"Cognitive exercises\",\n",
    "        \"Week 4\": \"Reassessment & goal setting\"\n",
    "    }\n",
    "    return triage, recovery_plan\n",
    "\n",
    "if st.button(\"Simulate Triage & Recovery Plan\"):\n",
    "    triage_result, plan = simulate_triage(age, severity, time_since_onset, symptoms)\n",
    "    st.subheader(\"2. Triage Priority\")\n",
    "    st.success(f\"Triage Level: {triage_result}\")\n",
    "\n",
    "    st.subheader(\"3. Suggested Recovery Plan\")\n",
    "    for week, activity in plan.items():\n",
    "        st.markdown(f\"**{week}:** {activity}\")\n",
    "\n",
    "    st.info(\"This is a simulated output. Not for clinical use.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
