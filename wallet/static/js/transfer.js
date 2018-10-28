window.artyom = new Artyom();
        let phone,money;
        if (localStorage.getItem('voice')) {
            artyom.addCommands([
                {
                    indexes: ['*'],
                    smart: true,
                    action: (i, wildcard) => {
                        console.log(wildcard)
                        let str = wildcard.split(" ");
                        console.log(str.length);
                        if (str.length == 4) 
                        {
                            document.getElementById('userToTransfer').value=str[0];
                            document.getElementById('moneyToTransfer').value=str[2];
                            document.transfer.submit();
                        }
                         else {
                            artyom.say('Please speak in correct format')
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
            artyom.say("say the reciever's name and money", {
                onStart: () => {
                    console.log("okay")
                },
            });
        }