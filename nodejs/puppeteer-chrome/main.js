const puppeteer = require('puppeteer-core');
const {aegisblade, Capability} = require('aegisblade');

/**
 * In this example the `runPuppeteer()` function will be run on a
 * server using AegisBlade.
 * 
 * @param {string} url The url to visit using puppeteer.
 */
async function runPuppeteer(url) {

    // Launch Puppeteer with a recommended set of flags.
    const browser = await puppeteer.launch({
        executablePath: 'google-chrome',
        headless: false,
        args: [
            '--no-sandbox',                 // REQUIRED, no sandbox is setup
            '--disable-setuid-sandbox',     // REQUIRED, no sandbox is setup
            '--single-process',             // REQUIRED, puppeteer crashes without this flag
            '--no-first-run',               // OPTIONAL, speeds up launch
            '--no-zygote',                  // OPTIONAL, removes the zygote process
            '--disable-dev-shm-usage'       // OPTIONAL, https://github.com/GoogleChrome/puppeteer/blob/master/docs/troubleshooting.md#tips
            ]
        });

    const page = await browser.newPage();
    await page.goto(url);

    let title = await page.title();
    console.log(title);

    await browser.close();

    return title;
}

// Any target function to be run on AegisBlade must be exported.
module.exports = {runPuppeteer};

/**
 * The `main()` function will run on your local machine
 * and start the job running the `runPuppeteer()` function
 * on a server using AegisBlade.
 */
async function main() {
    let jobConfig = {
        capabilities: [Capability.chrome]
    };

    let job = await aegisblade.run(runPuppeteer, ['https://nodejs.org/en/'], jobConfig);
    
    console.log(`Job Id: ${job.id}`);
    console.log("Waiting for the job to finish running...");

    let jobReturnValue = await job.getReturnValue();
    console.log(`Job Return Value: ${jobReturnValue}`);
    console.log(`Job Logs: ${await job.getLogs()}`);
}

//  Using the `require.main === module` idiom to only run main when this script
//    is called directly is especially important when using AegisBlade to prevent
//    infinite loops of jobs creating jobs.
if (require.main === module) {
    (async () => {
        try {
            await main();
        } catch (err) {
            console.error(err);
        }
    })();
}


