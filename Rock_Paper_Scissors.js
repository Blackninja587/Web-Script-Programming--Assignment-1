let userSelection = prompt("I challenge you to a game of Rock, Paper, Scissors. Pick your weapon of choice: ");
console.log("You chose: " + userSelection);

let random = Math.random()
let computerSelection = random;

if (computerSelection >= 0 && computerSelection <= 0.34) {
    console.log("The engine chose: Paper");
    if (userSelection == "Rock") {
        document.write("The engine triumphs")
    }
    if (userSelection == "Paper") {
        document.write("It is a tie, today there is no winner")
    }
    if (userSelection == "Scissors") {
        document.write("You have bested the engine, Congratulations")
    }
} else if (computerSelection >= 0.35 && computerSelection <= 0.67) {
    console.log("The engine chose: Scissors");
    if (userSelection == "Paper") {
        document.write("The engine triumphs")
    }
    if (userSelection == "Scissors") {
        document.write("It is a tie, today there is no winner")
    }
    if (userSelection == "Rock") {
        document.write("You have bested the engine, Congratulations")
    }
} else {
    console.log("The engine chose: Rock");
    if (userSelection == "Scissors") {
        document.write("The engine triumphs")
    }
    if (userSelection == "Rock") {
        document.write("It is a tie, today there is no winner")
    }
    if (userSelection == "Paper") {
        document.write("You have bested the engine, Congratulations")
    }
}