function money1(money){
    if (money < 13.95) {
        console.log("error");
    } 

    else {
        var amountofthreepacks = Math.floor(money/13.95);
       
    } 
        if (amountofthreepacks < 1){
            money = Math.floor(money/13.95);
            console.log("single cans:" + money);
        }
        
        else {
            var moneyforthreepacks = amountofthreepacks*30;
            var moneyforsinglecan = money - moneyforthreepacks;
        }

            if (moneyforsinglecan < 13.95){
                console.log(amountofthreepacks  + "Amount of three packs");
            }
            else {
                var amountofsinglecans = Math.floor(moneyforsinglecan/13.95);
                console.log("The amount of single cans is:"+ amountofsinglecans + "The amount of three packs is:" + amountofthreepacks);
            }


}
money1(347)