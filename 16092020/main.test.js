function numeroDeErdos(publicacoes){
  const autores = {erdos: 0}
  publicacoes.forEach(pub => {
    if (pub.includes('erdos')) {
      pub.forEach( autor => {
        if ( autor !== 'erdos'){
          autores[autor] = 1;
        }
        // if (pub.includes(autor))
      })
    } else {
      var peso = -1;
      pub.forEach( autor => {
        if (autor in autores) {
           if (autores[autor] < peso && peso !== -1) {
             peso = autores[autor];
           }
        }
      })
      pub.forEach( autor => {
        if (autores[autor] > peso && peso !== -1){
          autores[autor] = peso+1;
        } else if (!(autor in autores)) {
          autores[autor] = peso;
        }
      })
    }
  });
  return autores;
}
  
test('erdos possui o numero de erdos igual a 0', () => {
  expect(numeroDeErdos([['erdos']])).toStrictEqual({'erdos': 0});
});

test('coautor com erdos tem numero 1', () => {
  let publicacoes = [
    ['erdos', 'autor1']
  ];
  expect(numeroDeErdos(publicacoes)).toStrictEqual({'erdos': 0, 'autor1': 1});
});

test('coautor com erdos tem numero 1, duas publicações', () => {
  let publicacoes = [
    ['erdos'],
    ['erdos', 'autor1']
  ];
  expect(numeroDeErdos(publicacoes)).toStrictEqual({'erdos': 0, 'autor1': 1});
});

test('autor1 tem numero inf', () => {
  let publicacoes = [
    ['erdos'],
    ['autor1']
  ];
  expect(numeroDeErdos(publicacoes)).toStrictEqual({'erdos': 0, 'autor1': -1});
});

test('autor1 e autor2 tem numero inf', () => {
  let publicacoes = [
    ['erdos'],
    ['autor1', 'autor2']
  ];
  expect(numeroDeErdos(publicacoes)).toStrictEqual({ 'erdos': 0, 'autor1': -1, 'autor2': -1 });
});

test('autor1 e autor2 tem numero 1', () => {
  let publicacoes = [
    ['erdos', 'autor1', 'autor2'],
  ];
  expect(numeroDeErdos(publicacoes)).toStrictEqual({ 'erdos': 0, 'autor1': 1, 'autor2': 1 });
});

test('autor1 tem numero 1 e autor2 tem numero 2', () => {
  let publicacoes = [
    ['erdos', 'autor1'],
    ['autor1', 'autor2'],
  ];
  expect(numeroDeErdos(publicacoes)).toStrictEqual({ 'erdos': 0, 'autor1': 1, 'autor2': 2 });
});


// entrada:
// [
//   ['erdos', 'autor1'],
//   ['autor1', 'autor2'],
//   ['auto3'],
//   ['autor1', 'autor3']
// ]

// saida
// {
//   erdos: 0,
//   autor1: 1,
//   autor2: 2,
// }

// O Número de Erdos é uma homenagem prestada ao grande matemático húngaro Paul Erdos, que publicou em toda sua vida mais artigos do que qualquer outro matemático trabalhando com centenas de colaboradores. Este número, que mede a 'distância colaborativa' entre um autor de um artigo e Paul Erdos, é calculado da seguinte maneira:

// Erdos possui o número de Erdos igual a 0;
// Um matemático M possui esse número igual a soma de 1 com o menor número de Erdos dos matemáticos que escreveram um artigo junto com M;
// Aquele(a) que nunca escreveu nenhum artigo com Erdos ou com algum matemático que tenha escrito com Erdos ou com um matemático que escreveu com outro que tenha escrito com Erdos, e assim sucessivamente, tem número de Erdos infinito.
// Existem 511 matemáticos com número de Erdos igual a 1, ou seja, que escreveram artigos em parceria com Erdos. Os matemáticos que escreveram artigos junto com estes, possuem esse número igual a 2, os que escreveram artigos junto com estes últimos, possuem o número igual a 3, e assim por diante.

// Escreva um programa que, dada uma lista de publicações e seus autores, calcule o número de Erdos de cada autor.
