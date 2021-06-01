from vmc import *
from State import *
import matplotlib.pyplot as plt


def run_vmc(start_alpha, samples, iterations, learning_rate, metropolis_step):

    psi = State(start_alpha)
    vmc = Sampler()
    samples_number = samples
    iteration_number = iterations
    learning_rate = learning_rate

    optimized_energy = []

    for i in range(iteration_number):
        vmc.SetPsi(psi)

        elocs = np.zeros(samples_number)
        psider = np.zeros(samples_number)

        for n in range(samples_number):
            vmc.Step(metropolis_step)

            elocs[n] = (vmc.LocalEnergy())
            psider[n] = (psi.DerLog(vmc.x))

        energy = np.mean(elocs)
        eloc_der_mean = np.mean(elocs*psider)
        eloc_mean_der_mean = energy*np.mean(psider)
        elocder = eloc_der_mean - eloc_mean_der_mean
        psi.alpha = (psi.alpha - learning_rate * elocder)

        optimized_energy.append(energy)
        # print(f"alpha  = {psi.alpha}", )
        # print(f"energy = {energy}, variance = {np.std(elocs)}")
        # print(f"gradient variance = {np.std(elocder)}"'\n')

    return optimized_energy


if __name__ == "__main__":
    start_alpha = -1
    smaples_numb = 1000
    iterations_numb = 100
    lr = 0.5
    metropolis_step = 0.1
    optimized_ener = run_vmc(start_alpha, smaples_numb, iterations_numb, lr, metropolis_step)

    plt.plot(optimized_ener)
    plt.axhline(0.5, color='black')
    plt.ylabel('Energy')
    plt.xlabel('#Iteration')
    plt.show()

