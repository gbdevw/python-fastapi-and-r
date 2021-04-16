#* @post /crypto/<product>/predict
#* @serializer unboxedJSON
predict <- function(current_price, product){
  list(
        product = product,
        current_price = as.numeric(current_price),
        forecasted_price = as.numeric(current_price) + 5.0*(as.numeric(current_price)/100.0)
  )
}

#* @get /health
#* @serializer unboxedJSON
health <- function(){
  res.status = 200
  res.body = list(status_code=200, message="R sidecar OK")
}