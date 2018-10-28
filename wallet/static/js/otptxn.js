window.artyom = new Artyom();
        if (localStorage.getItem('voice')) {
            console.log('here')
            artyom.addCommands([
                {
                    indexes: ['*'],
                    smart: true,
                    action: (i, wildcard) => {
                        let str = wildcard;
                        let otp = str.split(" ").join("");
                        console.log(otp);
                        if (otp.length == 6) {
                           document.getElementById('otp').value=otp;
                           setTimeout(()=>{
                            document.otpVerify.submit();
                           },10000)
                        }else{
                            artyom.say('Please try again')
                        }
                    }

                }
            ])
            artyom.initialize({
                lang: "en-US", // GreatBritain english
                continuous: true, // Listen forever
                soundex: true,// Use the soundex algorithm to increase accuracy
                debug: true, // Show messages in the console
                executionKeyword: "and do it now",
                listen: true, // Start to listen commands !
                name: ""
            }).then(() => {
                console.log("Artyom has been succesfully initialized");
            }).catch((err) => {
                console.error("Artyom couldn't be initialized: ", err);
            });

            /**
             * To speech text
             */
            artyom.say("Enter OTP recieved on your mobile number", {
                onStart: () => {
                    console.log("Reading ...");
                },
            });
        }