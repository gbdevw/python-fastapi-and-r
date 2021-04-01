#* @post /crypto/<product>/predict
#* @serializer unboxedJSON
function(current_price, product){
  list(
        product = product,
        current_price = current_price,
        forecasted_price = current_price + 5*(current_price/100)
  )
}