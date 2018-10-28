window.artyom = new Artyom();
        artyom.on(['I want to login', 'I need to login']).then((i) => {
            switch (i) {
                case 0:
                    window.location = '/login'
                    break;
                case 1:
                    window.location = '/login'
                    break;
            }
        });

        // Smart command (Short code artisan way), set the second parameter of .on to true
        artyom.on(['Repeat after me *'], true).then((i, wildcard) => {
            artyom.say("You've said : " + wildcard);
        });

        // or add some commandsDemostrations in the normal way
        artyom.addCommands([
            {
                indexes: ['I want a voice Assistant', 'Yes I want a voice assistant', 'Yeah I need a voice assistant','Yeah'],
                action: (i) => {
                    artyom.say("Okay what kind of help do you need?");
                    localStorage.setItem('voice',true)
                }
            },
            {
                indexes: ['login *'],
                smart: true,
                action: (i, wildcard) => {
                    window.location = '/login'
                }
            },
            // The smart commands support regular expressions
            {
                indexes: [/Good Morning/i],
                smart: true,
                action: (i, wildcard) => {
                    artyom.say("You've said : " + wildcard);
                }
            },
            {
                indexes: ['no','no I dont need voice assisstant'],
                action: (i, wildcard) => {
                    artyom.fatality().then(() => {
                        console.log("Artyom succesfully stopped");
                    });
                }
            },
        ]);

        // Start the commands !
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
        artyom.say("Welcome to Paydex...! Do you want a Voice Assisstant", {
            onStart: () => {
                console.log("Reading ...");
            },
        });