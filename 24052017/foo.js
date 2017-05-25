function testarTeoria (teoria, resposta) {
  var feedback = [];
  if (teoria.s !== resposta.s) {
    feedback.push(1);
  }

  if (teoria.l !== resposta.l){
    feedback.push(2);
  }

  if (teoria.a !== resposta.a){
    feedback.push(3);
  }

  if (!feedback.length){
    feedback.push(0)
  }

  return feedback[Math.floor(Math.random() * feedback.length)];
}

function descobrirTeoria (resposta) {
  var suspeitos = [1,2,3,4];
  var locais = [1,2,3,4];
  var armas = [1,2,3,4,5,6,7];

  var achou = false;

  for (var i = suspeitos.length - 1; i >= 0 && !achou; i--) {
    for (var j = locais.length - 1; j >= 0 && !achou; j--) {
      for (var k = armas.length - 1; k >= 0 && !achou; k--) {
        var teste = testarTeoria(
          {
            s:suspeitos[i],
            l:locais[j],
            a:armas[k]
          },
          resposta
        );

        if (teste == 0) {
          achou = true;
        }
      }
    }
  }

  if (!achou) {
    return {}
  }


  return resposta;
}

module.exports = {
  testarTeoria, descobrirTeoria };