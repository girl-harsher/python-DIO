// let nivelFome = parseInt(prompt("digite o nivel da sua fome"));

// if (nivelFome === 1) {
//     console.log("voce esta com pouca fome")
// } else if (nivelFome === 2) {
//     console.log("muita fome")
// } else if (nivelFome === 3) {
//     console.log("ta cagado de fome")
// } else {
//     console.log("sei la ne porra escolhe um nivel entre 1 e 3")
// }

escolherBebida = "opcao"
    let valor;

    switch (opcao) {
        case 'café':
            valor = 3.50;
            break;
        case 'leite':
            valor = 2.00;
            break;
        case 'chá':
            valor = 2.50;
            break;
        default:
            console.log("Opção inválida. Escolha entre café, leite ou chá.");
            return; // Encerra a execução da função se a opção for inválida
    }

    console.log(`Você escolheu ${opcao}. O valor a ser pago é R$ ${valor.toFixed(2)}.`);
}

escolherBebida('café');
escolherBebida('leite');
escolherBebida('chá');
escolherBebida('refrigerante');

//////////////////////////////////////////////////////////////////////////////////////////////////////

let resultado = soma(5, 10)

console.log(resultado)

function soma(numA, numB){
	let somatorio = numA + numB
    return somatorio
}

/////////////////////////////////////////////////////////////////////////////////////////////////////

let userName = getFirstName("Esther-Garcia", "-")
console.log("Seja bem vindo " + userName)

userName = getFirstName("Esther Garcia", " ")
console.log("Seja bem vindo " + userName)

function getFirstName(name, splitChar){
	let firstName = name.split(splitChar)[0]
    return firstName
}
