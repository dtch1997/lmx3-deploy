"""Configuration for running RHPO"""
import ml_collections


def get_config():
    config = ml_collections.ConfigDict()
    config.domain = "humanoid"
    config.task = "run"

    config.max_num_actor_steps = int(1.5e7)
    config.eval_every = 5000
    config.seed = 0

    config.log_to_wandb = False
    config.wandb_project = "hpo"
    config.wandb_entity = "ethanluoyc"
    config.wandb_name = None

    # RHPO parameters
    config.num_components = 2
    config.tanh_mean = False
    config.critic_type = "nondistributional"
    config.network_type = "rhpo"
    config.policy_loss_config = dict(
        epsilon=0.1,
        epsilon_mean=0.0005,
        epsilon_stddev=0.00001,
        epsilon_categorical=0.0001,
        init_log_alpha_categorical=100.0,
        categorical_constraining=True,
    )
    return config


def get_sweep(h):
    del h
    sweep = []
    for domain, task in [
        ("humanoid", "stand"),
        ("humanoid", "walk"),
        ("humanoid", "run"),
    ]:
        for seed in [0, 1, 2]:
            for num_components in [1, 3, 5]:
                for tanh_squash in [False, True]:
                    sweep.append(
                        {
                            "config.domain": domain,
                            "config.task": task,
                            "config.num_components": num_components,
                            "config.seed": seed,
                            "config.tanh_mean": tanh_squash,
                        }
                    )
    return sweep