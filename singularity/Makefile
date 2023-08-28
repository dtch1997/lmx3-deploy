# The directory of the project to be built, relative to the Makefile
PROJECT_DIR ?= $(shell pwd)/../examples/jax_cuda
IMAGE_TAG ?= cuda
IMAGE_NAME ?= jax
DOCKER_NOCACHE ?= 0 # Usage: DOCKER_NOCACHE=1 make build-docker

DOCKER_NOCACHE_OPT = $(if $(filter 1,$(DOCKER_NOCACHE)),--no-cache,)

.PHONY: build-docker
build-docker:
	docker buildx build $(DOCKER_NOCACHE_OPT) \
		--tag $(IMAGE_NAME):$(IMAGE_TAG) \
		-f Dockerfile \
		$(PROJECT_DIR)

.PHONY: build-singularity
build-singularity: build-docker
	docker save $(IMAGE_NAME):$(IMAGE_TAG) -o image.tar	
	singularity build $(PROJECT_DIR)/cluster/$(IMAGE_NAME)-$(IMAGE_TAG).sif docker-archive://image.tar
	rm image.tar

.PHONY: clean-singularity
clean-singularity:
	rm *.sif

.PHONY: clean
clean:
	rm -rf build .cache
