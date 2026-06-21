async function askAgent() {

    const q = document.getElementById("question").value;

    const response = await fetch(
        "http://127.0.0.1:8000/ask?question=" + q
    );

    const data = await response.json();

    document.getElementById("answer").innerText =
        data.answer;
}