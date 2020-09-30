using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using UMWebApplication.Models;

namespace UMWebApplication.Controllers
{
    public class SpeakerController : Controller
    {
        // GET: Speaker
        public ActionResult Index()
        {
            using (UMWEBDBEntities1 db = new UMWEBDBEntities1())
            {
                return View(db.speakers.ToList());
            }
        }

        // GET: Speaker/Details/5
        public ActionResult Details(int? id)
        {
            using (UMWEBDBEntities1 db = new UMWEBDBEntities1())
            {
                return View(db.speakers.Where(x => x.id == id).FirstOrDefault());
            }
        }

        // GET: Speaker/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Speaker/Create
        [HttpPost]
        public ActionResult Create(speaker s)
        {
            try
            {
                using (UMWEBDBEntities1 ab = new UMWEBDBEntities1())
                {
                    ab.speakers.Add(s);
                    ab.SaveChanges();

                }

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }

        // GET: Speaker/Edit/5
        public ActionResult Edit(int? id)
        {
            using (UMWEBDBEntities1 db = new UMWEBDBEntities1())
            {
                return View(db.speakers.Where(x => x.id == id).FirstOrDefault());
            }
        }

        // POST: Speaker/Edit/5
        [HttpPost]
        public ActionResult Edit(int? id, speaker sp)
        {
            try
            {
                using (UMWEBDBEntities1 a = new UMWEBDBEntities1())
                {
                    a.Entry(sp).State = EntityState.Modified;
                    a.SaveChanges();
                }

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }

        // GET: Speaker/Delete/5
        public ActionResult Delete(int? id)
        {
            using (UMWEBDBEntities1 b = new UMWEBDBEntities1())
            {
                return View(b.speakers.Where(x => x.id == id).FirstOrDefault());
            }
        }

        // POST: Speaker/Delete/5
        [HttpPost]
        public ActionResult Delete(int id, FormCollection collection)
        {
            try
            {
                using (UMWEBDBEntities1 ab = new UMWEBDBEntities1())
                {
                    speaker s = ab.speakers.Where(x => x.id == id).FirstOrDefault();
                    ab.speakers.Remove(s);
                    ab.SaveChanges();
                }

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }
    }
}
