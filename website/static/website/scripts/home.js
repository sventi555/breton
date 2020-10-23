function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function crackerClick(e) {

    let cracker = e.target;
    let crackerBite = document.getElementById('cracker-bite');

    cracker.classList.add('hidden');
    crackerBite.classList.remove('hidden');

    await sleep(500);
    window.location.href = '/hello';
}

document.getElementById('cracker-box').onclick = crackerClick;
