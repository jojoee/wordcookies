/* global Handlebars, $ */

const $result = $('#result')
const $formSelector = 'form#form'
const $input = $('input#inp')
const $resultHdbTemplate = $('#result-hdbtemplate')
const resultHdbTemplate = Handlebars.compile($resultHdbTemplate.html())

function render (data) {
  let html = ''

  if (data) {
    for (const key of Object.keys(data)) {
      const n = key
      const words = data[key]

      if (words.length >= 1) {
        html += resultHdbTemplate({
          n: n,
          words
        })
      }
    }
  }

  $result.html(html)
}

$(document).on('submit', $formSelector, function (e) {
  // prevent
  e.preventDefault()

  // get input
  const inp = $input.val()
  const target = `/api/solve/${inp}`

  // get result
  $.get(target, function (res) {
    render(res.data)
  })
})
