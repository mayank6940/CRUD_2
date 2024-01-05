
const questions = document.querySelectorAll(".question");

questions.forEach(question => {
    question.addEventListener("click", () => {
        const answer = question.nextElementSibling;
        
        
        questions.forEach(otherQuestion => {
            if (otherQuestion !== question) {
                otherQuestion.classList.remove("expanded");
                otherQuestion.nextElementSibling.classList.remove("visible");
            }
        });

        
        question.classList.toggle("expanded");
        answer.classList.toggle("visible");

       
        if (answer.classList.contains("visible")) {
            answer.scrollIntoView({ behavior: "smooth" });
        }
    });
});
