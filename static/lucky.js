"use strict";

const HOSTNAME = "http://localhost:5001/api/get-lucky-num"

/** processForm: handle submission of form:
 *
 * - make API call to server to get num/year
 * - show errors, if errors are returned
 * - else: show results
 **/
async function processForm(evt) {
  evt.preventDefault();

  const response = await axios({
    url: `${HOSTNAME}`,
    method: "POST",
    data: {
      name: $("#name").val(),
      email: $("#email").val(),
      year: $("#year").val(),
      color: $("#color").val().toLowerCase(),
    },
  })

  const rd = response.data;

  ("error" in rd) ? showErrors(rd.error) : showResults(rd.num, rd.year);

}

/** showErrors: show error messages in DOM. */
function showErrors(error) {
  $("#lucky-results").text("");
  $(".error").text("");
  if ("name" in error) $("#name-err").text(error.name);
  if ("email" in error) $("#email-err").text(error.email);
  if ("color" in error) $("#color-err").text(error.color);
  if ("year" in error) $("#year-err").text(error.year);
}

/** showResults: show num and year in the DOM. */
function showResults(num, year) {
  $(".error").text("");
  $("#lucky-results").text("");
  $("#lucky-results").text(`Your lucky number is ${num.num} (${num.fact}).
  Your birth year (${year.year}) fact is ${year.fact}.`
  )
}


$("#lucky-form").on("submit", processForm);
