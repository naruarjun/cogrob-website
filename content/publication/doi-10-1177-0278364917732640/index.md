---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Distributed mapping with privacy and communication constraints: Lightweight
  algorithms and object-based models'
subtitle: ''
summary: ''
authors:
- Siddharth Choudhary
- Luca Carlone
- Carlos Nieto
- John Rogers
- Henrik I Christensen
- Frank Dellaert
tags: []
categories: []
date: '2017-01-01'
lastmod: 2022-12-07T21:14:44Z
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-12-07T21:14:44.455187Z'
publication_types:
- '2'
abstract: ' We consider the following problem: a team of robots is deployed in an
  unknown environment and it has to collaboratively build a map of the area without
  a reliable infrastructure for communication. The backbone for modern mapping techniques
  is pose graph optimization, which estimates the trajectory of the robots, from which
  the map can be easily built. The first contribution of this paper is a set of distributed
  algorithms for pose graph optimization: rather than sending all sensor data to a
  remote sensor fusion server, the robots exchange very partial and noisy information
  to reach an agreement on the pose graph configuration. Our approach can be considered
  as a distributed implementation of a two-stage approach that already exists, where
  we use the Successive Over-Relaxation and the Jacobi Over-Relaxation as workhorses
  to split the computation among the robots. We also provide conditions under which
  the proposed distributed protocols converge to the solution of the centralized two-stage
  approach. As a second contribution, we extend the proposed distributed algorithms
  to work with the object-based map models. The use of object-based models avoids
  the exchange of raw sensor measurements (e.g. point clouds or RGB-D data) further
  reducing the communication burden. Our third contribution is an extensive experimental
  evaluation of the proposed techniques, including tests in realistic Gazebo simulations
  and field experiments in a military test facility. Abundant experimental evidence
  suggests that one of the proposed algorithms (the Distributed Gauss–Seidel method)
  has excellent performance. The Distributed Gauss–Seidel method requires minimal
  information exchange, has an anytime flavor, scales well to large teams (we demonstrate
  mapping with a team of 50 robots), is robust to noise, and is easy to implement.
  Our field tests show that the combined use of our distributed algorithms and object-based
  models reduces the communication requirements by several orders of magnitude and
  enables distributed mapping with large teams of robots in real-world problems. The
  source code is available for download at https://cognitiverobotics.github.io/distributed-mapper/'
publication: '*The International Journal of Robotics Research*'
doi: 10.1177/0278364917732640
---
