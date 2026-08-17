from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
import pandas as pd
import tkinter as tk
from tkinter import ttk
from sklearn.naive_bayes import MultinomialNB
import difflib

df = pd.read_csv("diseases_dataset.csv")

X = df.drop("disease", axis=1)
y = df["disease"]

model = MultinomialNB()

model.fit(X, y)

y_pred = model.predict(X)

accuracy = accuracy_score(y, y_pred)

report = classification_report(
    y,
    y_pred,
    zero_division=0
)

cm = confusion_matrix(
    y,
    y_pred
)

root = tk.Tk()
root.title("🩺 Smart Disease Prediction Assistant")
root.geometry("1000x750")
root.configure(bg="#0f172a")

selected_lang = tk.StringVar(value="English")

disease_names={

"English":{

"Flu":"Flu",
"Common Cold":"Common Cold",
"Migraine":"Migraine",
"COVID-19":"COVID-19",
"Food Poisoning":"Food Poisoning",
"Constipation":"Constipation",
"Gastric Problem":"Gastric Problem",
"Heart Disease":"Heart Disease",
"Dengue":"Dengue",
"Typhoid":"Typhoid",
"Malaria":"Malaria",
"Asthma":"Asthma",
"Pneumonia":"Pneumonia",
"Diabetes":"Diabetes",
"Chicken Pox":"Chicken Pox",
"Allergy":"Allergy",
"Hypertension":"Hypertension",
"Anemia":"Anemia",
"Cancer":"Cancer"

},

"Hindi":{

"Flu":"फ्लू",
"Common Cold":"सामान्य सर्दी",
"Migraine":"माइग्रेन",
"COVID-19":"कोविड-19",
"Food Poisoning":"फूड पॉइजनिंग",
"Constipation":"कब्ज",
"Gastric Problem":"गैस की समस्या",
"Heart Disease":"हृदय रोग",
"Dengue":"डेंगू",
"Typhoid":"टाइफाइड",
"Malaria":"मलेरिया",
"Asthma":"अस्थमा",
"Pneumonia":"निमोनिया",
"Diabetes":"मधुमेह",
"Chicken Pox":"चेचक",
"Allergy":"एलर्जी",
"Hypertension":"उच्च रक्तचाप",
"Anemia":"एनीमिया",
"Viral Disease":"विषाणु रोग",
"Cancer":"कैंसर"

},

"Assamese":{

"Flu":"ফ্লু",
"Common Cold":"সাধাৰণ ঠাণ্ডা",
"Migraine":"মাইগ্ৰেইন",
"COVID-19":"কোভিড-১৯",
"Food Poisoning":"খাদ্য বিষক্ৰিয়া",
"Constipation":"কোষ্ঠকাঠিন্য",
"Gastric Problem":"গেছৰ সমস্যা",
"Heart Disease":"হৃদৰোগ",
"Dengue":"ডেংগু",
"Typhoid":"টাইফয়েড",
"Malaria":"মেলেৰিয়া",
"Asthma":"এজমা",
"Pneumonia":"নিউমোনিয়া",
"Diabetes":"ডায়েবেটিছ",
"Chicken Pox":"চিকেন পক্স",
"Allergy":"এলাৰ্জি",
"Hypertension":"উচ্চ ৰক্তচাপ",
"Anemia":"ৰক্তাল্পতা",
"Viral Disease":"ভাইৰেল ৰোগ",
"Cancer":"কেঞ্চাৰ"

},

"Bengali":{

"Flu":"ফ্লু",
"Common Cold":"সাধারণ সর্দি",
"Migraine":"মাইগ্রেন",
"COVID-19":"কোভিড-১৯",
"Food Poisoning":"খাদ্যে বিষক্রিয়া",
"Constipation":"কোষ্ঠকাঠিন্য",
"Gastric Problem":"গ্যাসের সমস্যা",
"Heart Disease":"হৃদরোগ",
"Dengue":"ডেঙ্গু",
"Typhoid":"টাইফয়েড",
"Malaria":"ম্যালেরিয়া",
"Asthma":"অ্যাজমা",
"Pneumonia":"নিউমোনিয়া",
"Diabetes":"ডায়াবেটিস",
"Chicken Pox":"চিকেন পক্স",
"Allergy":"অ্যালার্জি",
"Hypertension":"উচ্চ রক্তচাপ",
"Anemia":"রক্তস্বল্পতা",
"Viral Disease":"ভাইরাল রোগ",
"Cancer":"ক্যান্সার"

}

}

for lang in disease_names:
    for d in y.unique():
        disease_names[lang].setdefault(d,d)

medicine={
"English":{},
"Hindi":{},
"Assamese":{},
"Bengali":{}
}

diet={
"English":{},
"Hindi":{},
"Assamese":{},
"Bengali":{}
}

precautions={
"English":{},
"Hindi":{},
"Assamese":{},
"Bengali":{}
}

medicine["English"]={

"Flu":"Paracetamol, ORS, Vitamin C",
"Common Cold":"Paracetamol, Cough syrup, Vitamin C",
"Migraine":"Pain reliever (doctor advice preferred)",
"COVID-19":"Paracetamol, ORS",
"Food Poisoning":"ORS, Probiotics",
"Constipation":"Fiber supplement, Mild laxative",
"Gastric Problem":"Antacid",
"Heart Disease":"No self-medication, consult doctor",
"Dengue":"ORS, Fluids",
"Typhoid":"Doctor prescribed antibiotics",
"Malaria":"Doctor prescribed antimalarial medicine",
"Asthma":"Inhaler (doctor prescribed)",
"Pneumonia":"Doctor prescribed antibiotics",
"Diabetes":"Doctor prescribed medicine",
"Chicken Pox":"Calamine lotion",
"Allergy":"Antihistamine",
"Hypertension":"Doctor prescribed BP medicine",
"Anemia":"Iron supplement",
"Cancer":"Consult oncologist immediately. Treatment may include surgery, chemotherapy, radiotherapy or immunotherapy."
}

diet["English"]={

"Flu":"Soup, fruits, warm water",
"Common Cold":"Vitamin C fruits, ginger tea",
"Migraine":"Drink water, avoid caffeine",
"COVID-19":"Protein-rich foods, fruits",
"Food Poisoning":"Rice, banana, toast",
"Constipation":"Fiber-rich foods, vegetables",
"Gastric Problem":"Low spice food, yogurt",
"Heart Disease":"Low-fat food, oats",
"Dengue":"Papaya leaf juice, kiwi, fluids",
"Typhoid":"Soft food, boiled vegetables",
"Malaria":"High protein diet",
"Asthma":"Warm fluids",
"Pneumonia":"Soup, fruits",
"Diabetes":"Low sugar diet",
"Chicken Pox":"Soft foods",
"Allergy":"Vitamin C foods",
"Hypertension":"Low salt diet",
"Anemia":"Iron-rich foods",
"Cancer":"Protein-rich foods, fruits, vegetables and adequate hydration."
}

precautions["English"]={

"Flu":"Take rest and stay hydrated",
"Common Cold":"Avoid cold drinks",
"Migraine":"Avoid stress and bright light",
"COVID-19":"Wear mask and isolate",
"Food Poisoning":"Drink clean water",
"Constipation":"Drink more water",
"Gastric Problem":"Avoid spicy food",
"Heart Disease":"Avoid heavy exercise",
"Dengue":"Avoid mosquito bites",
"Typhoid":"Maintain hygiene",
"Malaria":"Use mosquito nets",
"Asthma":"Avoid dust",
"Pneumonia":"Take rest",
"Diabetes":"Monitor sugar regularly",
"Chicken Pox":"Avoid scratching",
"Allergy":"Avoid allergens",
"Hypertension":"Reduce salt intake",
"Anemia":"Take iron-rich foods",
"Cancer":"Seek medical attention immediately and follow doctor's advice."
}

for lang in medicine:

    for disease in y.unique():

        medicine[lang].setdefault(
        disease,
        "Consult doctor"
        )

        diet[lang].setdefault(
        disease,
        "Healthy balanced diet"
        )

        precautions[lang].setdefault(
        disease,
        "Take proper rest"
        )

medicine={

"English":{
"Flu":"Paracetamol, ORS, Vitamin C",
"Common Cold":"Paracetamol, Cough syrup, Vitamin C",
"Migraine":"Pain reliever (doctor advice preferred)",
"COVID-19":"Paracetamol, ORS",
"Food Poisoning":"ORS, Probiotics",
"Constipation":"Fiber supplement, Mild laxative",
"Gastric Problem":"Antacid",
"Heart Disease":"No self-medication, consult doctor",
"Dengue":"ORS, Fluids",
"Typhoid":"Doctor prescribed antibiotics",
"Malaria":"Doctor prescribed antimalarial medicine",
"Asthma":"Inhaler (doctor prescribed)",
"Pneumonia":"Doctor prescribed antibiotics",
"Diabetes":"Doctor prescribed medicine",
"Chicken Pox":"Calamine lotion",
"Allergy":"Antihistamine",
"Hypertension":"Doctor prescribed BP medicine",
"Anemia":"Iron supplement",
"Cancer":"Consult oncologist immediately. Treatment may include surgery, chemotherapy, radiotherapy or immunotherapy."
},

"Hindi":{
"Flu":"पैरासिटामोल, ORS, विटामिन C",
"Common Cold":"पैरासिटामोल, खांसी की दवा",
"Migraine":"दर्द निवारक",
"COVID-19":"पैरासिटामोल, ORS",
"Food Poisoning":"ORS, प्रोबायोटिक्स",
"Constipation":"फाइबर सप्लीमेंट",
"Gastric Problem":"एंटासिड",
"Heart Disease":"डॉक्टर से सलाह लें",
"Dengue":"ORS, तरल पदार्थ",
"Typhoid":"डॉक्टर द्वारा दी गई दवा",
"Malaria":"मलेरिया की दवा",
"Asthma":"इनहेलर",
"Pneumonia":"डॉक्टर द्वारा दी गई दवा",
"Diabetes":"डॉक्टर द्वारा दी गई दवा",
"Chicken Pox":"कैलामाइन लोशन",
"Allergy":"एंटीहिस्टामिन",
"Hypertension":"बीपी की दवा",
"Anemia":"आयरन सप्लीमेंट",
"Cancer":"तुरंत ऑन्कोलॉजिस्ट से संपर्क करें।"

},

"Assamese":{
"Flu":"পেৰাচিটামল, ORS, ভিটামিন C",
"Common Cold":"পেৰাচিটামল, কাহৰ ঔষধ",
"Migraine":"বিষ হ্ৰাসকাৰী ঔষধ",
"COVID-19":"পেৰাচিটামল, ORS",
"Food Poisoning":"ORS, প্ৰোবায়োটিক",
"Constipation":"ফাইবাৰ সম্পূৰক",
"Gastric Problem":"এণ্টাচিড",
"Heart Disease":"ডাক্তৰৰ পৰামৰ্শ লওক",
"Dengue":"ORS, বেছি পানী",
"Typhoid":"ডাক্তৰৰ ঔষধ",
"Malaria":"মেলেৰিয়া ঔষধ",
"Asthma":"ইনহেলাৰ",
"Pneumonia":"ডাক্তৰৰ ঔষধ",
"Diabetes":"ডাক্তৰৰ ঔষধ",
"Chicken Pox":"কেলামাইন লোচন",
"Allergy":"এণ্টিহিষ্টামিন",
"Hypertension":"BP ঔষধ",
"Anemia":"আয়ৰণ সম্পূৰক",
"Cancer":"তৎক্ষণাৎ কেঞ্চাৰ বিশেষজ্ঞৰ পৰামৰ্শ লওক।"

},

"Bengali":{
"Flu":"প্যারাসিটামল, ORS, ভিটামিন C",
"Common Cold":"প্যারাসিটামল, কাশির ওষুধ",
"Migraine":"ব্যথানাশক ওষুধ",
"COVID-19":"প্যারাসিটামল, ORS",
"Food Poisoning":"ORS, প্রোবায়োটিক",
"Constipation":"ফাইবার সাপ্লিমেন্ট",
"Gastric Problem":"অ্যান্টাসিড",
"Heart Disease":"ডাক্তারের পরামর্শ নিন",
"Dengue":"ORS, তরল খাবার",
"Typhoid":"ডাক্তারের ওষুধ",
"Malaria":"ম্যালেরিয়ার ওষুধ",
"Asthma":"ইনহেলার",
"Pneumonia":"ডাক্তারের ওষুধ",
"Diabetes":"ডাক্তারের ওষুধ",
"Chicken Pox":"ক্যালামাইন লোশন",
"Allergy":"অ্যান্টিহিস্টামিন",
"Hypertension":"BP ওষুধ",
"Anemia":"আয়রন সাপ্লিমেন্ট",
"Cancer":"অবিলম্বে ক্যান্সার বিশেষজ্ঞের পরামর্শ নিন।"
}

}

diet={

"English":{
"Flu":"Soup, fruits, warm water",
"Common Cold":"Vitamin C fruits, ginger tea",
"Migraine":"Drink water, avoid caffeine",
"COVID-19":"Protein-rich foods, fruits",
"Food Poisoning":"Rice, banana, toast",
"Constipation":"Fiber-rich foods, vegetables",
"Gastric Problem":"Low spice food, yogurt",
"Heart Disease":"Low-fat food, oats",
"Dengue":"Papaya leaf juice, kiwi, fluids",
"Typhoid":"Soft food, boiled vegetables",
"Malaria":"High protein diet",
"Asthma":"Warm fluids",
"Pneumonia":"Soup, fruits",
"Diabetes":"Low sugar diet",
"Chicken Pox":"Soft foods",
"Allergy":"Vitamin C foods",
"Hypertension":"Low salt diet",
"Anemia":"Iron-rich foods",
"Cancer":"Protein-rich foods, fruits, vegetables and adequate hydration."
},

"Hindi":{
"Flu":"सूप, फल, गर्म पानी",
"Common Cold":"विटामिन C वाले फल",
"Migraine":"पानी पिएं, कैफीन से बचें",
"COVID-19":"प्रोटीन युक्त भोजन",
"Food Poisoning":"चावल, केला",
"Constipation":"फाइबर युक्त भोजन",
"Gastric Problem":"कम मसाले वाला भोजन",
"Heart Disease":"कम वसा वाला भोजन",
"Dengue":"पपीते का रस",
"Typhoid":"उबला हुआ भोजन",
"Malaria":"प्रोटीन युक्त भोजन",
"Asthma":"गर्म तरल पदार्थ",
"Pneumonia":"सूप और फल",
"Diabetes":"कम चीनी वाला भोजन",
"Chicken Pox":"नरम भोजन",
"Allergy":"विटामिन C वाला भोजन",
"Hypertension":"कम नमक वाला भोजन",
"Anemia":"आयरन युक्त भोजन",
"Cancer":"प्रोटीन युक्त भोजन, फल और सब्जियां।"
},

"Assamese":{
"Flu":"চুপ, ফলমূল, গৰম পানী",
"Common Cold":"ভিটামিন C ফলমূল",
"Migraine":"বেছি পানী খাব",
"COVID-19":"প্ৰটিনযুক্ত খাদ্য",
"Food Poisoning":"ভাত, কল",
"Constipation":"ফাইবাৰযুক্ত খাদ্য",
"Gastric Problem":"কম ঝাল খাদ্য",
"Heart Disease":"কম তেলীয়া খাদ্য",
"Dengue":"পেঁপে পাতৰ ৰস",
"Typhoid":"উতলোৱা খাদ্য",
"Malaria":"প্ৰটিনযুক্ত খাদ্য",
"Asthma":"গৰম পানীয়",
"Pneumonia":"চুপ আৰু ফল",
"Diabetes":"কম চেনি খাদ্য",
"Chicken Pox":"নরম খাদ্য",
"Allergy":"ভিটামিন C খাদ্য",
"Hypertension":"কম নিমখ খাদ্য",
"Anemia":"আয়ৰণযুক্ত খাদ্য",
"Cancer":"প্ৰটিনযুক্ত খাদ্য, ফলমূল আৰু শাক-পাচলি।"
},

"Bengali":{
"Flu":"স্যুপ, ফল, গরম জল",
"Common Cold":"ভিটামিন C ফল",
"Migraine":"বেশি জল পান করুন",
"COVID-19":"প্রোটিনযুক্ত খাবার",
"Food Poisoning":"ভাত, কলা",
"Constipation":"ফাইবারযুক্ত খাবার",
"Gastric Problem":"কম মশলাযুক্ত খাবার",
"Heart Disease":"কম চর্বিযুক্ত খাবার",
"Dengue":"পেঁপে পাতার রস",
"Typhoid":"সেদ্ধ খাবার",
"Malaria":"প্রোটিনযুক্ত খাবার",
"Asthma":"গরম তরল খাবার",
"Pneumonia":"স্যুপ ও ফল",
"Diabetes":"কম চিনি খাবার",
"Chicken Pox":"নরম খাবার",
"Allergy":"ভিটামিন C খাবার",
"Hypertension":"কম লবণযুক্ত খাবার",
"Anemia":"আয়রনযুক্ত খাবার",
"Cancer":"প্রোটিনযুক্ত খাবার, ফল ও শাকসবজি।"
}

}

precautions={

"English":{
"Flu":"Take rest and stay hydrated",
"Common Cold":"Avoid cold drinks",
"Migraine":"Avoid stress and bright light",
"COVID-19":"Wear mask and isolate",
"Food Poisoning":"Drink clean water",
"Constipation":"Drink more water",
"Gastric Problem":"Avoid spicy food",
"Heart Disease":"Avoid heavy exercise",
"Dengue":"Avoid mosquito bites",
"Typhoid":"Maintain hygiene",
"Malaria":"Use mosquito nets",
"Asthma":"Avoid dust",
"Pneumonia":"Take rest",
"Diabetes":"Monitor sugar regularly",
"Chicken Pox":"Avoid scratching",
"Allergy":"Avoid allergens",
"Hypertension":"Reduce salt intake",
"Anemia":"Take iron-rich foods",
"Cancer":"Seek medical attention immediately and follow doctor's advice."
},

"Hindi":{
"Flu":"आराम करें और पानी पिएं",
"Common Cold":"ठंडी चीजों से बचें",
"Migraine":"तनाव से बचें",
"COVID-19":"मास्क पहनें और अलग रहें",
"Food Poisoning":"साफ पानी पिएं",
"Constipation":"अधिक पानी पिएं",
"Gastric Problem":"मसालेदार भोजन से बचें",
"Heart Disease":"भारी व्यायाम से बचें",
"Dengue":"मच्छरों से बचें",
"Typhoid":"सफाई बनाए रखें",
"Malaria":"मच्छरदानी का उपयोग करें",
"Asthma":"धूल से बचें",
"Diabetes":"शुगर जांच करें",
"Chicken Pox":"खुजली न करें",
"Allergy":"एलर्जी वाली चीजों से बचें",
"Hypertension":"कम नमक लें",
"Anemia":"आयरन युक्त भोजन लें",
"Cancer":"तुरंत डॉक्टर से सलाह लें और उपचार शुरू करें।"
},

"Assamese":{
"Flu":"বিশ্ৰাম লওক আৰু পানী খাব",
"Common Cold":"ঠাণ্ডা বস্তু এৰক",
"Migraine":"চাপ কম কৰক",
"COVID-19":"মাস্ক পিন্ধক আৰু পৃথক থাকক",
"Food Poisoning":"পৰিষ্কাৰ পানী খাব",
"Constipation":"বেছি পানী খাব",
"Gastric Problem":"ঝাল খাদ্য এৰক",
"Heart Disease":"ভাৰী ব্যায়াম এৰক",
"Dengue":"মহৰ পৰা সাৱধান থাকক",
"Typhoid":"পৰিষ্কাৰতা ৰাখক",
"Malaria":"মহৰ জাল ব্যৱহাৰ কৰক",
"Asthma":"ধূলিৰ পৰা দূৰত থাকক",
"Diabetes":"চেনি পৰীক্ষা কৰক",
"Chicken Pox":"খজুৱাব নালাগে",
"Allergy":"এলাৰ্জি বস্তু এৰক",
"Hypertension":"কম নিমখ খাব",
"Anemia":"আয়ৰণযুক্ত খাদ্য খাব",
"Cancer":"তৎক্ষণাৎ ডাক্তৰৰ পৰামৰ্শ লওক আৰু চিকিৎসা আৰম্ভ কৰক।"
},

"Bengali":{
"Flu":"বিশ্রাম নিন এবং জল পান করুন",
"Common Cold":"ঠান্ডা খাবার এড়ান",
"Migraine":"চাপ এড়িয়ে চলুন",
"COVID-19":"মাস্ক পরুন এবং আলাদা থাকুন",
"Food Poisoning":"পরিষ্কার জল পান করুন",
"Constipation":"বেশি জল পান করুন",
"Gastric Problem":"মশলাযুক্ত খাবার এড়ান",
"Heart Disease":"ভারী ব্যায়াম এড়ান",
"Dengue":"মশা থেকে বাঁচুন",
"Typhoid":"পরিষ্কার-পরিচ্ছন্ন থাকুন",
"Malaria":"মশারি ব্যবহার করুন",
"Asthma":"ধুলো এড়িয়ে চলুন",
"Diabetes":"নিয়মিত সুগার পরীক্ষা করুন",
"Chicken Pox":"চুলকাবেন না",
"Allergy":"অ্যালার্জি সৃষ্টি করে এমন জিনিস এড়ান",
"Hypertension":"কম লবণ খান",
"Anemia":"আয়রনযুক্ত খাবার খান",
"Cancer":"দ্রুত ডাক্তারের পরামর্শ নিন এবং চিকিৎসা শুরু করুন।"
}

}

for lang in medicine:

    for disease in y.unique():

        medicine[lang].setdefault(
            disease,
            medicine[lang].get(
                "Flu",
                "Consult doctor"
            )
        )

        diet[lang].setdefault(
            disease,
            diet[lang].get(
                "Flu",
                "Healthy balanced diet"
            )
        )

        precautions[lang].setdefault(
            disease,
            precautions[lang].get(
                "Flu",
                "Take proper rest"
            )
        )

def correct_text(text):

    words=text.lower().split()

    vocab=[]

    for col in X.columns:
        vocab.extend(
            col.replace("_"," ").split()
        )

    corrected=[]

    for word in words:

        match=difflib.get_close_matches(
            word,
            vocab,
            n=1,
            cutoff=0.75
        )

        corrected.append(
            match[0] if match else word
        )

    return " ".join(corrected)


def text_to_symptoms(text):

    text=text.lower()

    return {

    col:
    1 if col.replace(
    "_"," "
    ) in text

    else 0

    for col in X.columns

    }

header=tk.Frame(root,bg="#1e3a8a")
header.pack(fill="x")

tk.Label(
header,
text="🩺 Smart Disease Prediction Assistant",
font=("Segoe UI",22,"bold"),
bg="#1e3a8a",
fg="white"
).pack(pady=20)

card=tk.Frame(root,bg="#1e293b")
card.pack(fill="both",expand=True,padx=25,pady=25)

tk.Label(
card,
text="🌐 Select Language",
bg="#1e293b",
fg="white"
).pack()

ttk.Combobox(
card,
textvariable=selected_lang,
values=["English","Hindi","Assamese","Bengali"],
state="readonly"
).pack(pady=10)

tk.Label(
card,
text="📝 Enter Symptoms",
bg="#1e293b",
fg="white"
).pack()

entry=tk.Entry(
card,
width=50,
font=("Segoe UI",13),
bg="#334155",
fg="white",
insertbackground="white"
)

entry.pack(ipady=10)

result_label=tk.Label(
card,
text="",
justify="left",
font=("Segoe UI",11),
bg="#1e293b",
fg="#22c55e"
)

result_label.pack(pady=20)

def predict():

    text=entry.get()

    values=list(
    text_to_symptoms(
    correct_text(text)
    ).values()
    )

    if sum(values)==0:

        result_label.config(
        text="⚠ Symptoms not recognized"
        )

        return

    disease=model.predict(
    pd.DataFrame(
    [values],
    columns=X.columns
    )
    )[0]

    lang=selected_lang.get()

    result_label.config(

text=f"""

🧾 Disease:
{disease_names[lang][disease]}

💊 Medicine:
{medicine[lang][disease]}

🥗 Diet:
{diet[lang][disease]}

⚠ Precautions:
{precautions[lang][disease]}
"""
)
def show_metrics():

    metrics_window = tk.Toplevel(root)

    metrics_window.title("Model Evaluation")

    metrics_window.geometry("900x650")

    txt = tk.Text(
        metrics_window,
        font=("Consolas",10)
    )

    txt.pack(
        fill="both",
        expand=True
    )

    txt.insert(
        tk.END,
        f"""
=========================
MODEL EVALUATION
=========================

Accuracy : {accuracy*100:.2f} %

=========================
CLASSIFICATION REPORT
=========================

{report}

=========================
CONFUSION MATRIX
=========================

{cm}
"""
    )

    txt.config(state="disabled")

def clear():

    entry.delete(
    0,
    tk.END
    )

    result_label.config(
    text=""
    )

btn=tk.Frame(card,bg="#1e293b")
btn.pack()

tk.Button(
btn,
text="Predict",
bg="#22c55e",
fg="white",
command=predict
).grid(row=0,column=0,padx=10)

tk.Button(
btn,
text="Clear",
bg="#ef4444",
fg="white",
command=clear
).grid(row=0,column=1,padx=10)

tk.Button(
btn,
text="Metrics",
bg="#3b82f6",
fg="white",
command=show_metrics
).grid(row=0,column=2,padx=10)


root.mainloop()
