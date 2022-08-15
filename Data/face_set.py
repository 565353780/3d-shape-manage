#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Data.face import Face

class FaceSet(object):
    def __init__(self):
        self.face_list = []
        return

    def reset(self):
        self.face_list = []
        return True

    def getFaceIdx(self, face):
        if len(self.face_list) == 0:
            return None

        for i in range(len(self.face_list)):
            if not self.face_list[i].isSameFace(face):
                continue
            return i

        return None

    def isHaveFace(self, face):
        face_idx = self.getFaceIdx(face)
        if face_idx is None:
            return False
        return True

    def addFace(self, point_idx_list, no_repeat=False):
        face = Face(point_idx_list)

        if no_repeat:
            if self.isHaveFace(face):
                return True

        self.face_list.append(face)
        return True

    def getFace(self, face_idx):
        if face_idx >= len(self.face_list):
            print("[ERROR][FaceSet::getFace]")
            print("\t face_idx out of range!")
            return None
        return self.face_list[face_idx]

    def getMappingFaceSet(self, face_idx_list, mapping_dict):
        mapping_face_set = FaceSet()
        for face_idx in face_idx_list:
            face = self.getFace(face_idx)
            if face is None:
                print("[ERROR][FaceSet::getMappingFaceSet]")
                print("\t getFace failed!")
                return None

            mapping_point_idx_list = face.getMappingPointIdxList(mapping_dict)
            if mapping_point_idx_list is None:
                print("[ERROR][FaceSet::getMappingFaceSet]")
                print("\t getMappingPointIdxList failed!")
                return None

            mapping_face_set.addFace(mapping_point_idx_list)
        return mapping_face_set

    def outputInfo(self, info_level=0):
        line_start = "\t" * info_level
        print(line_start + "[FaceSet]")
        print(line_start + "\t face_num =", len(self.face_list))
        return True

