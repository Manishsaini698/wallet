window.artyom = new Artyom();
        if (localStorage.getItem('voice')) {
            console.log('here')
            artyom.addCommands([
                {
                    indexes:['*'],
                    smart:true,
                    action:(i,wildcard)=>{
                        let str=wildcard;
                        let pho=str.split(" ").join("");
                        console.log(pho);
                        if(pho.length==10){
                            document.getElementById('phone').value=pho;
                            document.otpLoginL.submit();
                           /* fetch("127.0.0.1:6543/enterotp",{
                                method:"post",
                                headers:{
                                    'Accept':'application/json',
                                    'Content-Type':'application/json'
                                },
                                body:JSON.stringify({
                                    'phone':pho
                                })
                            })
                            .then(e=>console.log(e))
                            .catch(err=>console.log(err))*/
                        }
                        else{
                            artyom.say("Kripya dobara prayas kare")
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
            artyom.say("Kripya apna dus anko ka mobile number dale", {
                onStart: () => {
                    console.log("Reading ...");
                },
            });
        }