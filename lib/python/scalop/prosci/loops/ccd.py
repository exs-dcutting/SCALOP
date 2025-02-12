#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import sys
import os
import subprocess

import numpy

def get_rotmat_and_rmsd(cfrom, cto):
    cfrom = numpy.array(cfrom)
    cto = numpy.array(cto)
    
    assert len(cfrom) == len(cto)
    
    
    T_to = numpy.mean(cto, axis=0)
    T_from = numpy.mean(cfrom, axis=0)
    
    for i,c in enumerate(cto):
       cto[i] = c - T_to
    for i,c in enumerate(cfrom):
       cfrom[i] = c - T_from
    
    
    correlation_matrix = numpy.dot(cto.transpose(), cfrom)
    v, s, w = numpy.linalg.svd(correlation_matrix)
    
    is_reflection = (numpy.linalg.det(v) * numpy.linalg.det(w)) < 0.0
    if is_reflection:
        s[-1] = - s[-1]
        v[:,-1] = -v[:,-1]
    
    rotation_matrix = numpy.dot(v,w).transpose()
    
    E0 = sum(sum(cfrom * cfrom)) + sum(sum(cto * cto))
    rmsd_sq = (E0 - 2.0*sum(s)) / float(len(cfrom))
    rmsd = numpy.sqrt(max(rmsd_sq, 0.0))
    
    return T_from, T_to, rotation_matrix, rmsd

def get_rotmat(cfrom, cto):
    cfrom = numpy.array(cfrom)
    cto = numpy.array(cto)
    
    assert len(cfrom) == len(cto)
    
    
    T_to = numpy.mean(cto, axis=0)
    T_from = numpy.mean(cfrom, axis=0)
    
    for i,c in enumerate(cto):
       cto[i] = c - T_to
    for i,c in enumerate(cfrom):
       cfrom[i] = c - T_from
    
    
    correlation_matrix = numpy.dot(cto.transpose(), cfrom)
    v, s, w = numpy.linalg.svd(correlation_matrix)
    
    is_reflection = (numpy.linalg.det(v) * numpy.linalg.det(w)) < 0.0
    if is_reflection:
        #s[-1] = - s[-1]
        v[:,-1] = -v[:,-1]
    
    rotation_matrix = numpy.dot(v,w).transpose()
    
    
    return T_from, T_to, rotation_matrix


def superimpose(rfrom, rto):
  """
  Altered / Faster
  """
  cfrom = []
  cto   = []
  for r,q in zip(rfrom, rto):
    cfrom.append(r.N.xyz)
    cfrom.append(r.CA.xyz)
    cfrom.append(r.C.xyz)
    cto.append(q.N.xyz)
    cto.append(q.CA.xyz)
    cto.append(q.C.xyz)
    if r.O is not None and q.O is not None:
      cfrom.append(r.O.xyz)
      cto.append(q.O.xyz)
  
  T_from, T_to, rotmat, rmsd = get_rotmat_and_rmsd(cfrom, cto)
  
  return rmsd

def superimpose_withloop(rfrom, rto, loop):
  cfrom = []
  cto   = []
  for r,q in zip(rfrom, rto):
    cfrom.append(r.N.xyz)
    cfrom.append(r.CA.xyz)
    cfrom.append(r.C.xyz)
    cto.append(q.N.xyz)
    cto.append(q.CA.xyz)
    cto.append(q.C.xyz)
    if r.O is not None and q.O is not None:
      cfrom.append(r.O.xyz)
      cto.append(q.O.xyz)
  
  T_from, T_to, rotmat, rmsd = get_rotmat_and_rmsd(cfrom, cto)
  
  for r in loop:
    for a in r:
      a.xyz = numpy.dot(a.xyz - T_from, rotmat) + T_to

