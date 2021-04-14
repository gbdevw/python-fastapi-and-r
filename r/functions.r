#* @post /crypto/<product>/predict
#* @serializer unboxedJSON
function(current_price, product){
  list(
        product = product,
        current_price = as.numeric(current_price),
        forecasted_price = as.numeric(current_price) + 5.0*(as.numeric(current_price)/100.0)
  )
}